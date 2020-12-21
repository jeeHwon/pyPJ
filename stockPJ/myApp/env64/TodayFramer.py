import pandas as pd 
df1 = pd.read_csv("C:/myData/STStatus/stat2020-12-18.csv")
df2 = pd.read_csv("C:/myData/STStatus/stat2020-12-17.csv")
df3 = pd.read_csv("C:/myData/STStatus/stat2020-12-16.csv")
df4 = pd.read_csv("C:/myData/STStatus/stat2020-12-15.csv")
df5 = pd.read_csv("C:/myData/STStatus/stat2020-12-14.csv")

df6 = pd.read_csv("C:/myData/STStatus/stat2020-12-21.csv")

# 분석결과(201220) : 일주일 데이터 분석 결과 최적의 손절라인: X / 익절라인: 2.2%

dftmp = pd.concat([df1,df2,df3,df4,df5,df6])
# print(dftmp)
dftmp['HIGH_RATE'] = (dftmp['HIGH']-dftmp['BUY_UNIT'])/ dftmp['BUY_UNIT'] * 100
dftmp['LOW_RATE'] = (dftmp['LOW']-dftmp['BUY_UNIT'])/ dftmp['BUY_UNIT'] * 100
dftmp['CLOSE_RATE'] = (dftmp['CLOSE']-dftmp['BUY_UNIT'])/ dftmp['BUY_UNIT'] * 100
print(dftmp)

high = dftmp['HIGH_RATE'].values
low = dftmp['LOW_RATE'].values
close = dftmp['CLOSE_RATE'].values

df = pd.DataFrame({'HIGH': high, 'LOW': low, 'CLOSE':close})
print(df)
upline = 0.0
underline = -20.0 # 즉 손절라인 안주고 종가에 파는게 무조건 이득이라는 결론...
while(upline<4):
    suik = 0
    for row in df.itertuples():
        # print(row[1], row[2])
        if row[2] >= underline:
            if row[1] >= upline:
                suik = suik + upline
            else:
                suik = suik + row[3]
        else:
            suik = suik + underline
        # suik = suik + row[3]
    print('upline:',upline, "=>", round(suik,2))
    upline = upline + 0.1   
