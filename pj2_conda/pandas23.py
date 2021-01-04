import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import font_manager, rc
from datetime import datetime

fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 시간계산
# now1 = datetime.now()
# print(now1)
# print(type(now1))
# s1 = now1.strftime("%Y-%m-%d")
# s2 = now1.strftime("%H:%M:%S")
# print(s1)
# print(s2)

# t1 = datetime(1991,7,18)
# print(t1)
# print(now1-t1)

# 파일형 변환(시간)
# 방법 1) 파일 읽어서 데이터 타입을 수정
# df = pd.read_csv('data/ebola.csv')
# df.info()
# print(df.head())
# df['Date'] = pd.to_datetime(df['Date'])
# df.info()
# print(df.head())

# 방법2) 읽을 때 바꿔서 읽기
# df = pd.read_csv('data/ebola.csv', parse_dates=['Date'])
# df.info()
# print(df.head())
# print(df['Date'][2])
# print(df['Date'][2].year)
# print(df['Date'][2].month)
# print(df['Date'][2].day)
# print(df['Date'][2].quarter)    # 몇분기인지
# print('에볼라 최초 발생일:', df['Date'].min())
# df['new'] = df['Date'] - df['Date'].min()
# print(df)


# 파산 은행 데이터
# bank = pd.read_csv('data/bank.csv')
# bank.info()
# print(bank.head())

# 연도별 파산한 은행수
bank = pd.read_csv('data/bank.csv', parse_dates=['Closing Date', 'Updated Date'])
bank.info()
bank['year'] = bank['Closing Date'].dt.year
# print(bank)
# print(bank.groupby('year').count())
# print(bank.groupby('year')['Bank Name'].count())
# print(bank.groupby('year').size())
# s1 = bank.groupby('year').size()
# plt.plot(s1)
# plt.xticks(list(range(2000,2020,2)))
# plt.show()

# 연도별 분기별 파산한 은행수
bank['quarter'] = bank['Closing Date'].dt.quarter
# print(bank)
s2 = bank.groupby(['year','quarter']).size()
# print(s2)
# print(type(s2))     # 시리즈
d2 = s2.reset_index()
# print(d2)
d2['new'] = d2['year'].astype(str)+'-'+d2['quarter'].astype(str)
print(d2)

plt.plot(d2['new'],d2[0]) # s2가 복합 인덱스여서 x축 
plt.title('연도별 분기별 파산한 은행수')
plt.show()