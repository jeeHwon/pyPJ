from os import write
import matplotlib.pyplot as plt 
from jeelib import Analyzer1
from numpy.lib.shape_base import column_stack
import pandas as pd
import csv
from datetime import datetime
from slacker import Slacker
import numpy as np 

mk = Analyzer1.MarketDB()
url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&serachType=13'
krx = pd.read_html(url, header=0)[0]
krx = krx[['종목코드', '회사명']]
krx = krx.rename(columns={'종목코드':'code', '회사명':'company'})
krx.code = krx.code.map('{:06d}'.format)
allCodes = krx.code.tolist()
# allCodes = ['005930']

def get_BB_list(date):
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
        df['II'] = (2*df['close']-df['high']-df['low']) / (df['high']-df['low'])*df['volume']
        df['IIP21'] = df['II'].rolling(window=21).sum() / df['volume'].rolling(window=21).sum() * 100
        df = df[19:]
        df = df.dropna()
        df['s_date'] = df['date'].apply(lambda x:x.strftime('%Y-%m-%d'))

        try:
            if df[df['s_date']==date]['PB'].values[0] > 0.90 and df[df['s_date']==date]['MFI10'].values[0]>90:
                buylist.append(c)
                print(c)
            elif df[df['s_date']==date]['PB'].values[0] < 0.10 and df[df['s_date']==date]['IIP21'].values[0]>0:
                buylist.append(c)
                print(c)
        except:
            print("err")
    return buylist
        

def get10dayDf(buylist, date, buyrate):
    temp = []
    for c in buylist:
        df = mk.get_daily_price(c, '2020-11-25')
        df['s_date'] = df['date'].apply(lambda x:x.strftime('%Y-%m-%d'))
        df['cha'] = (df['high']-df['low'])*buyrate
        s0 = [0]
        s0.extend(df['cha'].tolist())
        s0 = s0[:-1]
        df['cha'] = s0
        df = df[df['s_date']>=date]
        df = df.iloc[:10]
        df['t_price'] = df['open']+df['cha']
        temp.append(df)
    total_df = pd.concat(temp, ignore_index=False)
    return total_df

def getRate(data, up_line):
    suik = 0
    for code in buylist:
        isOk = False
        df = data[data['code']==code]
        buy_price = df.iloc[0]['t_price']
        for i in range(len(df)):
            if (df.iloc[i]['high'] / buy_price - 1 )*100 > up_line:
                suik = suik + up_line
                isOk = True
                break
        if isOk :
            continue
        suik = suik + (df.iloc[-1]['close'] / buy_price - 1 )*100
    return suik/len(buylist)

# ==main

target_date = "2020-12-21"

buylist = get_BB_list(target_date)
print(buylist)

# target date로 부터 10일치의 데이터
data = get10dayDf(buylist, target_date, 0.4)
print(data)

xlist = np.arange(0.1, 35.0, 0.1)
columns = ['up_line','suik']
rows = []
for i in range(0,len(xlist)):
    rows.append([xlist[i], getRate(data, xlist[i])])

fin = pd.DataFrame(rows, columns=columns)
plt.scatter(fin['up_line'], fin['suik'])
plt.show()
fin = fin.round(2)
fin = fin.sort_values('suik', ascending=False)
print(fin.head(10))


fin.to_csv("C:/myData/BB_rate_stat/{}.csv".format(target_date), index = False)
print(fin.head(10))


