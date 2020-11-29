import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
from Investar import Analyzer

# ---------------Input area---------------
RLTV_START_DATE = '2020-5-1'
RLTV_END_DATE = '2020-8-1'
ABS_START_DATE = RLTV_END_DATE
ABS_END_DATE = '2020-11-1'
STOCK_COUNT = 10
# ----------------------------------------

mk = Analyzer.MarketDB()
# 특정 기간 동안 수익률이 제일 높았던 stock_count개의 종목들(상대 모멘텀)
connection = pymysql.connect(host='localhost', port=3307, db='investar', user='root', passwd='asdf1038', autocommit=True)
cursor = connection.cursor()
sql = f"select max(date) from daily_price where date <= '{RLTV_START_DATE}'"
cursor.execute(sql)
result = cursor.fetchone()
if (result[0] is None):
    print("start_date : {} -> retured None".format(sql))
    
start_date = result[0].strftime('%Y-%m-%d')

sql = f"select max(date) from daily_price where date <='{RLTV_END_DATE}'"
cursor.execute(sql)
result = cursor.fetchone()
if (result[0] is None):
    print("end_date : {} -> retured None".format(sql))
    
end_date = result[0].strftime('%Y-%m-%d')

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
df = df.head(STOCK_COUNT)
df.index = pd.Index(range(STOCK_COUNT))

connection.close()
print(df)
print(f"\nRelative momentum ({start_date} ~ {end_date}) : {df['returns'].mean():2f}% \n")

# 특정 기간 동안 상대 모멘텀에 투자했을 때의 평균 수익률(절대 모멘텀)
stockList = list(df['code'])
connection = pymysql.connect(host='localhost', port=3307, db='investar', user='root', passwd='asdf1038', autocommit=True)
cursor = connection.cursor()
sql = f"select max(date) from daily_price where date <= '{ABS_START_DATE}'"
cursor.execute(sql)
result = cursor.fetchone()
if (result[0] is None):
    print("start_date : {} -> retured None".format(sql))
start_date = result[0].strftime('%Y-%m-%d')

sql = f"select max(date) from daily_price where date <='{ABS_END_DATE}'"
cursor.execute(sql)
result = cursor.fetchone()
if (result[0] is None):
    print("end_date : {} -> retured None".format(sql))
end_date = result[0].strftime('%Y-%m-%d')

rows = []
columns = ['code', 'company', 'old_price', 'new_price', 'returns']
for _, code in enumerate(stockList):
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
connection.close()
print(df)
print(f"\nAbsolute momentum ({start_date} ~ {end_date}) : {df['returns'].mean():2f}% \n")


