import pandas as pd 
import math
from datetime import datetime
import numpy as np
from pandas.core.series import Series
# ===AZ_1RsToSt.py===
# env32에서 크레온 계정 통해 금일 체결내역을 저장한 res와 pls 파일을 읽어,
# 날짜, 코드, 종목명, OHLC, 매수단가, 매도단가, 거래량, 손익, 수익률 컬럼의 데이터프레임으로 가공하여,
# stat 파일로 저장

# date = "2021-01-04"
date = datetime.today().strftime('%Y-%m-%d')
df = pd.read_csv("C:/myData/TodayResult/res{}.csv".format(date), error_bad_lines=False)
columns = ['DATE', 'CODE', 'NAME', 'OPEN','HIGH', 'LOW', 'CLOSE','BUY', 'SELL', 'QTY']
rows = []
rows.append([df.iloc[0][1],df.iloc[0][2],df.iloc[0][3],df.iloc[0][4],df.iloc[0][5],df.iloc[0][6],
    df.iloc[0][7],df.iloc[0][8]* df.iloc[0]['QTY'],df.iloc[0][9]* df.iloc[0]['QTY'],df.iloc[0][10]])
# print(rows)
for i in range(1, df.shape[0]):
    isJungbok = False
    for j in range(len(rows)):
        if df.iloc[i][2] == rows[j][1]:
            rows[j][7] = rows[j][7] + df.iloc[i]['BUY'] * df.iloc[i]['QTY']
            rows[j][8] = rows[j][8] + df.iloc[i]['SELL'] * df.iloc[i]['QTY']
            rows[j][9] = rows[j][9] + df.iloc[i]['QTY']
            isJungbok = True
            break
    if isJungbok == False:
        rows.append([df.iloc[i][1],df.iloc[i][2],df.iloc[i][3],df.iloc[i][4],df.iloc[i][5],df.iloc[i][6],
            df.iloc[i][7],df.iloc[i][8]* df.iloc[i]['QTY'],df.iloc[i][9]* df.iloc[i]['QTY'],df.iloc[i][10]])
df2 = pd.DataFrame(rows, columns=columns)
df2['QTY'] = df2['QTY']//2
tmp2 = []
tmp3 = []
for i in range(df2.shape[0]):
    tmp2.append(math.trunc(df2.iloc[i]['BUY']/df2.iloc[i]['QTY']))
    tmp3.append(math.trunc(df2.iloc[i]['SELL']/df2.iloc[i]['QTY']))
df2['BUY'] = tmp2
df2['SELL'] = tmp3

df3 = pd.read_csv("C:/myData/TodayResult/pls{}.csv".format(date), error_bad_lines=False)
pl = []
for i in range(df2.shape[0]):
    medo = 0
    mesu = 0
    for j in range(df3.shape[0]):
        if df2.iloc[i]['CODE'] == df3.iloc[j]['CODE']:
            if df3.iloc[j]['TYPE'] == "매도":
                medo = medo +  df3.iloc[j]['PL']
            elif df3.iloc[j]['TYPE'] == "매수":
                mesu = mesu +  df3.iloc[j]['PL']
    pl.append(medo - mesu)
df2['PL'] = Series(pl)
df2['ROI'] = df2['PL'] / (df2['BUY']*df2['QTY']) * 100
df2 = df2.round(2)
df2.to_csv("C:/myData/TodayStatus/stat{}.csv".format(date), index = False)
print(df2)