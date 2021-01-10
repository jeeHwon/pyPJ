import time
import sys, ctypes
import win32com.client
import pandas as pd
from datetime import datetime
import pymysql, calendar, json

cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')  # 종목코드
cpStatus  = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')  # 주문관련
cpStock = win32com.client.Dispatch("DsCbo1.StockMst")
cpOhlc = win32com.client.Dispatch("CpSysDib.StockChart")
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')    # 계좌 정보
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')   # 주문 가능 금액
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 

# 크레온 플러스 시스템 점검 함수
def check_creon_system():
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('check_creon_system() : admin user -> FAILED')
        return False

    # 연결여부 체크
    if (cpStatus.IsConnect == 0):
        print('check_creon_system() : connect to server -> FAILED')
        return False

    # 주문 관련 초기화 - 계좌 관련 코드가 있을 때만 사용
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system() : init trade -> FAILED')
        return False
    return True

check_creon_system()

def read_creon(code):
    """크레온 API에서 주식 시세를 읽어와서 데이터프레임으로 반환"""
    try:
        code = "A"+code
        cpOhlc.SetInputValue(0, code)               # 종목코드
        cpOhlc.SetInputValue(1, ord('2'))           # 1:기간, 2:개수
        cpOhlc.SetInputValue(4, 5)                # 요청 개수
        cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5, 6, 8, 37])    # 0:날짜, 2~5 OHLC
        cpOhlc.SetInputValue(6, ord('D'))           # D: 일단위
        cpOhlc.SetInputValue(9, ord('1'))           # 0: 무수정주가, 1:수정주가
        cpOhlc.BlockRequest()
        count = cpOhlc.GetHeaderValue(3) 
        columns = ['date','open','high','low','close','diff','volume']
        index = []
        rows = []
        for i in range(count):
            index.append(cpOhlc.GetDataValue(0, i))
            rows.append([cpOhlc.GetDataValue(0, i), cpOhlc.GetDataValue(1, i), cpOhlc.GetDataValue(2, i),
                cpOhlc.GetDataValue(3, i), cpOhlc.GetDataValue(4, i),cpOhlc.GetDataValue(5, i),
                cpOhlc.GetDataValue(6, i)])    
        df = pd.DataFrame(rows, columns=columns, index=index)
        
    except Exception as e:
        # print('Exception occured : ', str(e))
        return None
    return df

def read_krx_code():
    """KRX로부터 상장법인목록 파일을 읽어와서 데이터프레임으로 반환"""
    url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&serachType=13'
    krx = pd.read_html(url, header=0)[0]
    krx = krx[['종목코드', '회사명']]
    krx = krx.rename(columns={'종목코드':'code', '회사명':'company'})
    krx.code = krx.code.map('{:06d}'.format)
    return krx

def replace_into_db(df, num, code, company):
        """네이버 금융에서 읽어온 주식 시세를 DB에 replace"""
        with conn.cursor() as curs:
            for r in df.itertuples():
                sql = f"replace into daily_price values ('{code}', '{r.date}', {r.open}, {r.high}, {r.low}, {r.close}, {r.diff}, {r.volume})"
                curs.execute(sql)
            conn.commit()
            print('[{}] #{:04d} {} ({}) : {} rows > REPLACE INTO daily_price [OK]'.format(datetime.now().strftime('%Y-%m-%d %H:%M'), num+1, company, code, len(df)))

conn = pymysql.connect(host='localhost', port=3307, db='investar', user='root', passwd='1234', charset='utf8')
with conn.cursor() as curs:
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
conn.commit()
codes = dict()


sql = "select * from company_info"
df = pd.read_sql(sql, conn)
for idx in range(len(df)):
    codes[df['code'].values[idx]]=df['company'].values[idx]
with conn.cursor() as curs:
    sql = 'select max(last_update) from company_info'
    curs.execute(sql)
    rs = curs.fetchone()
    today = datetime.today().strftime('%Y-%m-%d')

    if  rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
        krx = read_krx_code()
        print(rs[0], krx)
        for idx in range(len(krx)):
            code = krx.code.values[idx]
            company = krx.company.values[idx]
            sql = f"replace into company_info (code, company, last_update) values ('{code}', '{company}', '{today}')"
            curs.execute(sql)
            codes[code] = company
            tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
            print(f"[{tmnow}] {idx:04d} REPLACE INTO company_info VALUES ({code}, {company}, {today})")
        conn.commit()
        print('')

for idx, code in enumerate(codes):
    df = read_creon(code)
    if df is None:
        continue
    replace_into_db(df, idx, code, codes[code])
    time.sleep(1)

print("-"*30)
time.sleep(100)