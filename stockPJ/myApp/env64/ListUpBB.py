from os import write
import matplotlib.pyplot as plt 
from jeelib import Analyzer1
import pandas as pd
import csv
from datetime import datetime
from slacker import Slacker

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
date = 0
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

    try:
        if df.PB.values[len(df.close)-1] > 0.90 and df.MFI10.values[len(df.close)-1]>90:
            buyok = buyok + 1
            buylist.append("A"+c)
        elif df.PB.values[len(df.close)-1] < 0.10 and df.IIP21.values[len(df.close)-1]>0:
            buyok = buyok + 1
            buylist.append("A"+c)
        else:
            buyno = buyno + 1
    except:
        buyerr = buyerr + 1

file_name = 'C:/myData/BuyList/BB_buylist.csv'
with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(buylist)

def getPwd():
    """텍스트 파일을 읽어 비밀번호 또는 코드를 입력한다."""
    with open ('C:\\myKey\\slackbot.txt') as f:
        pw = f.readline()
    return pw.strip()
slack = Slacker(getPwd())

def dbgout(message):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S]') + message
    slack.chat.post_message('#general', strbuf)

dbgout('ListUp된 종목:{}\n거절된 종목:{}\n에러:{}'.format(buyok, buyno, buyerr))

