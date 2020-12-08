import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
from Investar import Analyzer

mk = Analyzer.MarketDB()

def get_rltv_momentum(start_date, end_date, stock_count):
        """특정 기간 동안 수익률이 제일 높았던 stock_count개의 종목들(상대 모멘텀)
            - start_date : 상대 모멘텀을 구할 시작일자('2020-01-01')
            - end_date : 상대 모멘텀을 구할 종료일자('2020-12-31')
            - stock_count : 상대 모멘텀을 구할 종목수
        """
        connection = pymysql.connect(host='localhost', port=3307, db='investar', user='root', passwd='asdf1038', autocommit=True)
        cursor = connection.cursor()

        # 사용자가 입력한 시작일자를 DB에서 조회되는 일자로 보정
        sql = f"select max(date) from daily_price where date <= '{start_date}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if (result[0] is None):
            print("start_date : {} -> retured None".format(sql))
            return
        start_date = result[0].strftime('%Y-%m-%d')

        # 사용자가 입력한 종료일자를 DB에서 조회되는 일자로 보정
        sql = f"select max(date) from daily_price where date <='{end_date}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if (result[0] is None):
            print("end_date : {} -> retured None".format(sql))
            return
        end_date = result[0].strftime('%Y-%m-%d')

        # KRX 종목별 수익률을 구해서 2차원 리스트 형태로 추가
        rows = []
        columns = ['code', 'company', 'old_price', 'new_price', 'returns']
        for _, code in enumerate(mk.codes):
            sql = f"select close from daily_price where code='{code}' and date='{start_date}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if(result is None):
                continue
            old_price = int(result[0])

            sql = f"select close from daily_price where code='{code}' and date='{end_date}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if(result is None):
                continue
            new_price = int(result[0])
            returns = (new_price / old_price -1) * 100
            rows.append([code, mk.codes[code], old_price, new_price, returns])

        df = pd.DataFrame(rows, columns=columns)
        df = df[['code', 'company', 'old_price', 'new_price', 'returns']]
        df = df.sort_values(by='returns', ascending=False)
        df = df.head(stock_count)
        df.index = pd.Index(range(stock_count))

        connection.close()
        print(df)
        print(f"\nRelative momentum ({start_date} ~ {end_date}) : {df['returns'].mean():2f}% \n")

        return df