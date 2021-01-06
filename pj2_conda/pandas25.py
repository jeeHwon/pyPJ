import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import font_manager, rc
import seaborn as sns


fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)


# 매개변수 2이상 함수 적용
# def plus3(x):
#     return x+3

# def plusn(x,n):
#     return x+n

# def cal(x,n,m):
#     return (x+n)*m

# df = pd.DataFrame({'a':[1,2,3], 'b':[10,20,30]})
# print(df)
# print(df['a'].apply(plus3))
# print(df['a'].apply(plusn, x=10))
# print(df['a'].apply(cal, n=10, m=2))
# print(df.apply(cal,n=10,m=3))
# print(df.apply(cal,n=10,m=3,axis=1))


# def hap(x):
#     print(x)
#     print('-'*30)
#     return x.sum()

# df = pd.DataFrame({'name':['kim','park','kim','lee','jee'],
                            # 'grade':[1,2,1,2,3],
                            # 'kor':[10,20,35,40,80],
                            # 'eng':[10,20,30,40,90]})
# print(df)                            
# print(df.groupby(['name','grade']).apply(hap))          
# print(df.groupby(['name','grade'])['kor'].apply(hap))   # 학년과 이름이 같은 학생들의 국어 점수 합
# print(df.groupby(['name','grade'])['kor'].apply(lambda x:x.sum()))  # 위줄과 같은 코드


# agg(메서드)
# 여러개의 집계메서드를 한번에 사용
# def getAvg(x):
#     return x.mean()

# print(df.groupby('name')['kor'].apply(getAvg))  # 1
# print(df.groupby('name')['kor'].mean())         # 2
# print(df.groupby('name')['kor'].agg(getAvg))    # 3 1~3  모두 동일
# print(df.groupby('name')['kor'].agg(['sum','mean','median','std',getAvg]))
# print(df.groupby('name').agg({'kor':'sum', 'eng':'mean'}))
# print(df.groupby(['name','grade']).agg({'kor':['sum','mean','median','std'],
#                                         'eng':lambda x: x+33}))


# tips = sns.load_dataset('tips')
# print(tips.head())
# tips['rate'] = tips['tip']/tips['total_bill']
# print(tips['rate'])
# g1 = tips.groupby(['sex', 'smoker'])
# print(g1.agg({'total_bill':'mean',
#                 'tip':'std',
#                 'rate':'mean'}))

# print(list(range(1,100,10)))
# print(pd.date_range(start='2020-1-1', end='2020-12-31'))
# print(pd.date_range(start='2020-1-1', end='2020-12-31', freq='W-Mon'))

df = pd.read_csv('data/ebola.csv')
# df = df.head()
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.set_index('Date')
# df = df.reindex(pd.date_range(start='2014-3-21', end='2015-1-5'))
# print(df)
# plt.plot(df)
# plt.show()

df['Date'] = pd.to_datetime(df['Date'])
ebola = df.set_index('Date')
print(ebola.iloc[:,:5])
ebola = ebola.reindex(pd.date_range(start='2014-3-22',
                    end='2015-1-5'))
print(ebola.iloc[:5,:5])
print(pd.date_range(start='2021-1-1',
                    end='2021-12-31', freq='W'))
print(pd.date_range(start='2021-1-1',
                    end='2021-12-31', freq='B'))
