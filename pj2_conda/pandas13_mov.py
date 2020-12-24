from os import name
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pandas.core.reshape.merge import merge

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# # ml-m1 영화, 평점, 사용자 데이터 읽기
# movies = pd.read_csv('data/ml-1m/movies.dat', sep="::", 
#     names=['MovieID','Title','Genres'])

# ratings = pd.read_csv('data/ml-1m/ratings.dat', sep="::", 
#     names=['UserID','MovieID','Rating','Timestamp'])

# users = pd.read_csv('data/ml-1m/users.dat', sep="::", 
#     names=['UserID','Gender','Age','Occupation','Zip-code'])

# # movies + ratings
# mr = pd.merge(movies, ratings, on='MovieID')

# # (movies + ratings) + users
# mru = mr.merge(users, on='UserID')
# # mru.to_csv('data/mov2.csv', index=False, header=False)
# mru.to_csv('data/mov2.csv', index=False)

data = pd.read_csv('data/mov2.csv')
# print(data.columns)

# 영화 제목별 평점 건수
title_cnt = data.groupby('Title')['Rating'].size()
# print(title_cnt)  # 시리즈

# # tips 데이터에서 토, 일 팁만 추출
# tips = sns.load_dataset('tips')
# # print(tips)
# tips = tips.set_index('day')
# print(tips)
# print(tips.loc[['Sun', 'Sat']])
# # 요일별 식사건수
# g1 = tips.groupby('day').size()
# print(g1)
# # 식사건수가 50건 이상인 데이터만 가지고 분석
# g1 = g1[g1>=50]
# print(g1)
# print(g1.index)
# print(g1.values)

# 평점건수가 200건 이상 있는 영화 정보
# r200 = title_cnt[title_cnt>=200] # 평점건수가 200건 이상인 영화 타이틀을 r200에 저장
# # print(r200.index)
# data = data.set_index('Title')
# # print(data)
# data200 = data.loc[r200.index]  # 전체 데이터에서 인덱스가 r200 영화 타이틀
# # print(data200)
# data200 = data200.reset_index()
# # print(data200)

# 영화별 평균 평점
# print(data200.groupby('Title')['Rating'].mean())

# 성별에 따른 평균 평점
# print(data200.groupby(['Title', 'Gender'])['Rating'].mean())

# 여성에서 높은 평점을 받은 영화 5
# s1 = data200.groupby(['Title', 'Gender'])['Rating'].mean()
# d1 = s1.reset_index()
# d1 = d1[d1['Gender']=='F']
# # print(d1)
# d2 = d1.sort_values(by='Rating', ascending=False)
# print(d2.head())

# 타이타닉 데이터
titanic = sns.load_dataset('titanic')
# print(titanic)
# titanic.info()
# print(titanic['deck'])

# 누락값 : 데이터 없음
from numpy import NaN, nan, NAN
# print(NaN==True)
# print(NaN==False)
# print(NaN==0)
# print(NaN=='')        # 얘네로 쓰면 안돼

# print(pd.isnull(NAN)) # 얘네로 쓰자
# print(pd.isnull(NaN))
# print(pd.isnull(nan))
# print(pd.notnull(nan))

# 누락값의 개수
# print(titanic.count())  # 각 열의 값의 개수
print(titanic.shape[0]-titanic.count())  # 누락값의 개수