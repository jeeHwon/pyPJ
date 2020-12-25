import pymysql
import pandas as pd
from datetime import timedelta
from datetime import datetime
import re
import csv

def get_comp_info():
    """company_info 테이블에서 읽어와서 codes에 저장"""
    sql = "select * from company_info"
    krx = pd.read_sql(sql, conn)
    for idx in range(len(krx)):
        codes[krx['code'].values[idx]] = krx['company'].values[idx]

def get_daily_price(code_in, start_date=None, end_date=None):
    """KRX 종목별 시세를 데이터프레임 형태로 반환
        - code : KRX 종목코드('005930') 또는 상장기업명('삼성전자')
        - start_date : 조회 시작일('2020-01-01') 미입력시 30일 전 날짜
        - end_date : 조회 종료일('2020-12-31') 미입력시 오늘 날짜
    """
    if (start_date is None):
            one_month_ago = datetime.today() - timedelta(days=30)
            start_date = one_month_ago.strftime('%Y-%m-%d')
            # print("start_date is initialized to '{}'".format(start_date))
    else:
        start_lst = re.split('\D+', start_date)
        if(start_lst[0] == ''):
            start_lst = start_lst[1:]
        start_year = int(start_lst[0])
        start_month = int(start_lst[1])
        start_day = int(start_lst[2])
        if start_year < 1900 or start_year>2200:
            print(f"ValueError: start_year({start_year:d}) is wrong.")
            return
        if start_month < 1 or start_month>12:
            print(f"ValueError: start_month({start_month:d}) is wrong.")
            return
        if start_day < 1 or start_day>31:
            print(f"ValueError: start_day({start_day:d}) is wrong.")
            return
        start_date = f"{start_year:04d}-{start_month:02d}-{start_day:02d}"

    if (end_date is None or end_date==''):
        end_date = datetime.today().strftime('%Y-%m-%d')
        # print("end_date is initialized to '{}'".format(end_date))
    else:
        end_lst = re.split('\D+', end_date)
        if(end_lst[0] == ''):
            end_lst = end_lst[1:]
        end_year = int(end_lst[0])
        end_month = int(end_lst[1])
        end_day = int(end_lst[2])
        if end_year < 1800 or end_year>2200:
            print(f"ValueError: end_year({end_year:d}) is wrong.")
            return
        if end_month < 1 or end_month>12:
            print(f"ValueError: end_month({end_month:d}) is wrong.")
            return
        if end_day < 1 or end_day>31:
            print(f"ValueError: end_day({end_day:d}) is wrong.")
            return
        end_date = f"{end_year:04d}-{end_month:02d}-{end_day:02d}"

    # 회사명으로 종목코드 조회
    codes_keys = list(codes.keys())
    codes_values = list(codes.values())
    if code_in in codes_keys:
        pass
    elif code_in in codes_values:
        idx = codes_values.index(code)
        code_in = codes_keys[idx]
    else:
        print("ValueError: Code({}) doesnt`t exist.".format(code_in))

    sql = f"select * from daily_price where code='{code_in}' and date >= '{start_date}' and date <= '{end_date}'" 
    df = pd.read_sql(sql, conn)
    df.index = df['date']
    return df.sort_index(ascending=False)

conn = pymysql.connect(host='localhost', port=3307, db='investar', user='root', passwd='1234', charset='utf8')
codes={}
symbol_list=[]

get_comp_info()

# 모든 종목 추가
# symbol_list.extend(codes.values())

# 볼린저밴드 리스트 종목 추가
with open('C:/myApp/env64/BB_TF_buylist.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f) 
    for i,line in enumerate(rdr): 
        if i==0:
            for j in range(len(line)):
                tmp = line[j].replace("A","")
                symbol_list.append(tmp)

print('리스트 종목 수:',len(symbol_list)) 
columns = ['OVER', 'UNDER', 'ROI']
rows = []
overline = 20.0
underline = -20.0
kvalue = 0.30
while overline <= 21.0:
    total_roi = 0
    ok_cnt = 0
    err_cnt = 0
    for i in range(len(symbol_list)):
        try:
            code = symbol_list[i]
            # 리스트에 있는 종목 1개에 대하여 BP 찾기
            # 1) 변동성 돌파 지점 (kvalue)
            df = get_daily_price(code)
            today = df.iloc[0]
            lastday = df.iloc[1]

            today_open = today['open']
            lastday_high = lastday['high']
            lastday_low = lastday['low']
            target_price = today_open + (lastday_high - lastday_low) * kvalue

            # 2) ma5 및 ma10 돌파지점
            lastday_date = lastday.name
            closes = df['close'].sort_index()
            ma5 = closes.rolling(window=5).mean()
            ma5_price = ma5.loc[lastday_date]
            ma10 = closes.rolling(window=10).mean()
            ma10_price = ma10.loc[lastday_date]

            # 3) BP 구하기
            buy_price = max([target_price, ma5_price, ma10_price])
            # print('bp',buy_price)

            # 리스트에 있는 종목 1개에 대하여 SP 찾기
            overline_price = buy_price*(1+overline*0.01)
            underline_price = buy_price*(1+underline*0.01)

            if today['low']>=underline_price:
                if today['high'] >= overline_price:
                    sell_price = overline_price
                else:
                    sell_price = today['close']
            else:
                sell_price = underline_price

            # 리스트에 있는 종목 1개에 대하여 ROI 계산
            roi = (sell_price/buy_price-1)*100
            # print('roi',roi)
            total_roi = total_roi + roi
            ok_cnt += 1
            # print(total_roi)
        except:
            err_cnt += 1
    # print(ok_cnt, err_cnt)
    print(total_roi/ok_cnt)
    rows.append([overline, underline, total_roi/ok_cnt])
    underline += -1.0
    if underline <= -25.0:
        overline += 0.1
        underline = -20.0
        print("overline:",overline)

df2 = pd.DataFrame(rows, columns=columns).round(2)
kname = int(kvalue*100)
df2.to_csv("C:/myData/AZ_test.csv")
print(df2)

