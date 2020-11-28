import pandas as pd
from bs4 import BeautifulSoup
import urllib, pymysql, calendar, time, json
import pymysql
from urllib.request import urlopen
from datetime import datetime
from threading import Timer
import pymysql


class DBUpdater:
    def __init__(self):
        """생성자 : MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', port=3307, db='investar', user='root', passwd='asdf1038', charset='utf8')

        with self.conn.cursor() as curs:
            sql = """
            create table if not exists company_info(
                code varchar(20),
                company varchar(40),
                last_update date,
                primary key (code))
            """
            curs.execute(sql)
            sql = """
            create table if not exists daily_price(
                code varchar(20),
                date DATE,
                open bigint(20),
                high bigint(20),
                low bigint(20),
                close bigint(20),
                diff bigint(20),
                volume bigint(20),
                primary key (code, date))
            """
            curs.execute(sql)
        self.conn.commit()
        self.codes = dict()


    def __del__(self):
        """소멸자 : MariaDB 연결해제"""
        self.conn.close()


    def read_krx_code(self):
        """KRX로부터 상장법인목록 파일을 읽어와서 데이터프레임으로 반환"""
        url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&serachType=13'
        krx = pd.read_html(url, header=0)[0]
        krx = krx[['종목코드', '회사명']]
        krx = krx.rename(columns={'종목코드':'code', '회사명':'company'})
        krx.code = krx.code.map('{:06d}'.format)
        return krx


    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트한 후 딕셔너리에 저장"""
        sql = "select * from company_info"
        df = pd.read_sql(sql, self.conn)
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]]=df['company'].values[idx]
        with self.conn.cursor() as curs:
            sql = 'select max(last_update) from company_info'
            curs.execute(sql)
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')

            if  rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
                krx = self.read_krx_code()
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    sql = f"replace into company_info (code, company, last_update) values ('{code}', '{company}', '{today}')"
                    curs.execute(sql)
                    self.codes[code] = company
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f"[{tmnow}] {idx:04d} REPLACE INTO company_info VALUES ({code}, {company}, {today})")
                self.conn.commit()
                print('')


    def read_naver(self, code, company, pages_to_fetch):
        """네이버 금융에서 주식 시세를 읽어와서 데이터프레임으로 반환"""
        try:
            url = f'https://finance.naver.com/item/sise_day.nhn?code={code}'
            with urlopen(url) as doc:
                if doc is None:
                    return None
                html = BeautifulSoup(doc, 'lxml')
                pgrr = html.find('td', class_='pgRR')
                if pgrr is None:
                    return None
                s = str(pgrr.a['href']).split('=')
                lastpage = s[-1]
            df = pd.DataFrame()
            pages = min(int(lastpage), pages_to_fetch)
            

            for page in range(1, pages+1):
                pg_url = '{}&page={}'.format(url, page)
                df = df.append(pd.read_html(pg_url, header=0)[0])
                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}] {} ({}) : {:04d}/{:04d} pages are dowloading...'.format(tmnow, company, code, page, pages), end='\r')
                
            df = df.rename(columns={'날짜':'date', '종가':'close', '전일비':'diff', '시가':'open', '고가':'high', '저가':'low', '거래량':'volume'})
            df['date'] = df['date'].replace('.','-')
            df = df.dropna()
            df[['close','diff','open','high','low','volume']] = df[['close','diff','open','high','low','volume']].astype(int)
            df = df[['date','open','high','low','close','diff','volume']]
            
        except Exception as e:
            print('Exception occured : ', str(e))
            return None
        return df


    def replace_into_db(self, df, num, code, company):
        """네이버 금융에서 읽어온 주식 시세를 DB에 replace"""
        with self.conn.cursor() as curs:
            for r in df.itertuples():
                sql = f"replace into daily_price values ('{code}', '{r.date}', {r.open}, {r.high}, {r.low}, {r.close}, {r.diff}, {r.volume})"
                curs.execute(sql)
            self.conn.commit()
            print('[{}] #{:04d} {} ({}) : {} rows > REPLACE INTO daily_price [OK]'.format(datetime.now().strftime('%Y-%m-%d %H:%M'), num+1, company, code, len(df)))


    def update_daily_price(self, pages_to_fetch):
        """KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트"""
        for idx, code in enumerate(self.codes):
            df = self.read_naver(code, self.codes[code], pages_to_fetch)
            if df is None:
                continue
            self.replace_into_db(df, idx, code, self.codes[code])


    def execute_daily(self):
        """실행 즉시 및 매일 오후 다섯시에 daily_price 테이블 업데이트"""
        self.update_comp_info()
        try:
            with open('config.json', 'r') as in_file:
                config = json.load(in_file)
                pages_to_fetch = config['pages_to_fetch']
        except FileNotFoundError:
            with open('config.json', 'w') as out_file:
                pages_to_fetch = 100
                config = {'pages_to_fetch': 1}
                json.dump(config, out_file)
        self.update_daily_price(pages_to_fetch)

        tmnow = datetime.now()
        lastday = calendar.monthrange(tmnow.year, tmnow.month)[1]
        if tmnow.month == 12 and tmnow.day == lastday:
            tmnext = tmnow.replace(year=tmnow.year+1, month=1, day=1, hour=17, minute=0, second=0)
        elif tmnow.day == lastday:
            tmnext = tmnow.replace(month=tmnow.month+1, day=1, hour=17, minute=0, second=0)
        else:
            tmnext = tmnow.replace(day=tmnow.day+1, hour=17, minute=0, second=0)
        tmdiff = tmnext - tmnow
        secs = tmdiff.seconds

        t = Timer(secs, self.execute_daily)
        print("Waiting for next update({}) ...".format(tmnext.strftime('%Y-%m-%d %H:%M')))
        t.start()


if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()