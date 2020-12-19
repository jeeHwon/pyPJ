from os import write
import matplotlib.pyplot as plt 
from jeelib import Analyzer1
import pandas as pd
import csv

# ======================== ver 1.1 ========================

# 업데이트 : 20.12.18
# 현재 매일 250 ~ 300개의 종목수. 추세추종 줄이고, 반전매매 기법 추가 위해 수치 조정
# %b : 0.8 -> 0.85
# MFI : 80 -> 85

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
    df['TP'] = (df['high'] + df['low'] + df['close']) / 3
    df['PMF'] = 0
    df['NMF'] = 0
    for i in range(len(df.close)-1):
        if df.TP.values[i] < df.TP.values[i+1]:
            df.PMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]
            df.NMF.values[i+1] = 0
        else:
            df.NMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]
            df.PMF.values[i+1] = 0
    df['MFR'] = df.PMF.rolling(window=10).sum() / df.NMF.rolling(window=10).sum()
    df['MFI10'] = 100 - 100 / (1 + df['MFR'])
    df = df[19:]
    # print(df.date.values[-1])
    # break

    try:
        if df.PB.values[len(df.close)-1] > 0.85 and df.MFI10.values[len(df.close)-1]>85:
            buyok = buyok + 1
            buylist.append("A"+c)
        else:
            buyno = buyno + 1
    except:
        buyerr = buyerr + 1
print(buyok, buyno, buyerr)
file_name = 'C:/myApp/env64/BB_TF_buylist.csv'
with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(buylist)
