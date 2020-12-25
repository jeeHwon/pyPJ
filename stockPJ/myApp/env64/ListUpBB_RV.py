from os import write
import matplotlib.pyplot as plt 
from jeelib import Analyzer1
import pandas as pd
import csv

# ======================== ver 1.2 ========================
# 업데이트 : 20.12.25
# 경로 수정: C:/myData/BuyList/BB_TF_buylist.csv 
# %b : 0.10
# IIP21 : 0

mk = Analyzer1.MarketDB()
url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&serachType=13'
krx = pd.read_html(url, header=0)[0]
krx = krx[['종목코드', '회사명']]
krx = krx.rename(columns={'종목코드':'code', '회사명':'company'})
krx.code = krx.code.map('{:06d}'.format)
allCodes = krx.code.tolist()

buyok = 0
buyno = 0
buyerr = 0
buylist = []
for c in allCodes:
    df = mk.get_daily_price(c, '2020-11-01')
    df['MA20'] = df['close'].rolling(window=20).mean()
    df['stddev'] = df['close'].rolling(window=20).std()
    df['upper'] = df['MA20'] + (df['stddev'] * 2)
    df['lower'] = df['MA20'] - (df['stddev'] * 2)
    df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower'])

    df['II'] = (2*df['close']-df['high']-df['low']) / (df['high']-df['low'])*df['volume']
    df['IIP21'] = df['II'].rolling(window=21).sum() / df['volume'].rolling(window=21).sum() * 100
    df = df.dropna()

    try:
        if df.PB.values[len(df.close)-1] < 0.10 and df.IIP21.values[len(df.close)-1]>0:
            buyok = buyok + 1
            buylist.append("A"+c)
        else:
            buyno = buyno + 1
    except:
        buyerr = buyerr + 1
print(buyok, buyno, buyerr)
file_name = 'C:/myData/BuyList/BB_RV_buylist.csv'
with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(buylist)