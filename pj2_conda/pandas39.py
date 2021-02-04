import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

# 그래프처리 및 파일 로드
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)
d1 = pd.read_csv('data/accidentdata.csv')
d2 = pd.read_csv('data/ebola.csv')

print('==================문제1==================')
day_dead = d1.groupby('요일')['사망자수'].sum()
day_list = ['월','화','수','목','금','토','일']
day_dead = day_dead.reindex(day_list)
plt.figure(figsize=(20,10))
plt.title('요일별 교통사고 사망자수 합계')
plt.xlabel('요일')
plt.ylabel('사망자수')
sns.lineplot(x=day_dead.index, y=day_dead.values)
plt.show()

print('==================문제2==================')
byGu = d1[(d1['발생지시도']=='서울')&(d1['발생년']==2014)].groupby('발생지시군구')['사상자수'].sum()
print(byGu)
plt.figure(figsize=(20,10))
plt.title('2014년 서울지역 구별 교통사고 사상자수 합계')
plt.xlabel('구')
plt.ylabel('사상자수')
sns.barplot(x=byGu.index, y=byGu.values)
plt.show()

print('==================문제3==================')
print(d1.pivot_table(index='발생지시도', columns='발생년', values='사망자수' ,aggfunc='sum'))
plt.figure(figsize=(20,10))
plt.title('연도 및 발생지 시도별 교통사고 사망자수의 합')
plt.xlabel('발생지시도')
plt.ylabel('사망자수')
sns.barplot(data=d1, x='발생지시도', y='사망자수', hue='발생년', estimator=sum)
plt.show()

print('==================문제4==================')
print(d2.shape[0])
print(d2.shape[1])
print(d2.dtypes) 
d2.info()

print('==================문제5==================')
d2['Date'] = pd.to_datetime(d2['Date'])

print('==================문제6==================')
d2['yy'] = d2['Date'].dt.year
d2['mm'] = d2['Date'].dt.month
d2['dd'] = d2['Date'].dt.day
print(d2.head())

print('==================문제7==================')
year = d2[d2['Date'] == d2['Date'].min()]['yy'].values[0]
month = d2[d2['Date'] == d2['Date'].min()]['mm'].values[0]
day = d2[d2['Date'] == d2['Date'].min()]['dd'].values[0]
print('에볼라 최초 발생일: {}년 {}월 {}일'.format(year, month, day))

print('==================문제8==================')
d2 = d2.set_index(d2['Date'])
d2 = d2.reindex(pd.date_range(start=d2['Date'].min(), end=d2['Date'].max()))
print(d2)

print('==================문제9==================')
d2 = d2.fillna(0)
d2['Total_Deaths'] = d2['Deaths_Guinea'] +d2['Deaths_Liberia'] +d2['Deaths_SierraLeone'] +\
    d2['Deaths_Nigeria'] +d2['Deaths_Senegal'] +d2['Deaths_UnitedStates'] +d2['Deaths_Spain'] +d2['Deaths_Mali']
d2['Cumsum'] = d2['Total_Deaths'].cumsum()
plt.figure(figsize=(20,10))
plt.title('일자별 에볼라로 인한 사망자 수')
plt.xlabel('일자')
plt.ylabel('사망자수')
sns.lineplot(x=d2.index, y=d2.Cumsum)
plt.show()

print('==================문제10==================')
Ans_10 = """\
판다스 데이터 구조
판다스는 R을 모티브로 만든 파이썬 라이브러리로, 데이터 분석을 위한 수집, 전처리 과정에 사용된다.
판다스 데이터프레임의 하위 자료형으로 시리즈와 데이터프레임이 있다.
1) 시리즈(Series) : 
1개의 열로 구성되고 딕셔너리, 튜플, 리스트 형태로 쉽게 생성이 가능하다.
2) 데이터프레임(Dataframe) :
2개 이상의 열로 구성되고, 시리즈가 여러개 합쳐진 형태의 자료형이다.
--------------------------------------------------------------
판다스 데이터 타입(자료형 : 알리아스)
Datetime : datetime
Catogiriclal : category
Numeric : int64, float64.. 
String : string
Boolean : boolean
"""
print(Ans_10)