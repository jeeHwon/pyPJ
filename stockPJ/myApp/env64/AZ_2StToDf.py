import pandas as pd 
import csv
import numpy
import os

# ===AZ_2StToDf.py===
# 가공된 stat 파일을 읽어,
# 각 날짜별 High, Low, Close에 매도 하였을 경우의 수익률을 컬럼으로 추가하여, 
# 최대 수익률 내는 손절 및 익절라인을 구해 df_BestLine에 저장

path_dir = 'C:/myData/TodayStatus'
file_list = os.listdir(path_dir)
dftmp = []
for i in range(len(file_list)):
    df = pd.read_csv("C:/myData/TodayStatus/{}".format(file_list[i]))
    dftmp.append(df)

# 분석결과(201220) : 일주일 데이터 분석 결과 최적의 손절라인: X / 익절라인: 2.2%
# 분석결과(201222) : 손절라인:X / 익절라인: 1.3%

dftmp = pd.concat(dftmp)
print(dftmp)
dftmp['HIGH_RATE'] = (dftmp['HIGH']-dftmp['BUY'])/ dftmp['BUY'] * 100
dftmp['LOW_RATE'] = (dftmp['LOW']-dftmp['BUY'])/ dftmp['BUY'] * 100
dftmp['CLOSE_RATE'] = (dftmp['CLOSE']-dftmp['BUY'])/ dftmp['BUY'] * 100
# print(dftmp)

date = dftmp['DATE'].values
name = dftmp['NAME'].values
high = dftmp['HIGH_RATE'].values
low = dftmp['LOW_RATE'].values
close = dftmp['CLOSE_RATE'].values

df = pd.DataFrame({'DATE':date,'NAME':name,'HIGH': high, 'LOW': low, 'CLOSE':close})
# print(df.sort_values(by='HIGH'))
# print(df.sort_values(by='LOW'))
# print(df.sort_values(by='CLOSE'))
# print(df['HIGH'].max())
# print(df['LOW'].max())
# print(df['CLOSE'].max())

f = open('df_BestLine.csv','w', newline='')
wr = csv.writer(f)

xlist = numpy.arange(0.0, 25.0, 0.1)    # upline
ylist = numpy.arange(0.0, -20.0, -0.1)  # underline

wr.writerow(xlist.round(2))
f.close()

# print(len(xlist))
# print(type(ylist[2]))
for i in range(1,len(ylist)):
    tmp = []
    tmp.append(round(ylist[i],2))
    for j in range(1,len(xlist)):
        suik = 0
        for row in df.itertuples():
            if row[4] >= ylist[i]:
                if row[3] >= xlist[j]:
                    suik = suik + xlist[j]
                else:
                    suik = suik + row[5]    
            else:
                suik = suik + ylist[i]
        tmp.append(round(suik,2))
    f = open('df_BestLine.csv','a', newline='')
    wr = csv.writer(f)
    wr.writerow(tmp)
    f.close()

