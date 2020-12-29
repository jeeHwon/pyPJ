from os import name
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pandas.core.reshape.merge import merge

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 파일을 읽어 tmp에 각 데이터 프레임을 저장
tmp = []
for year in range(1880, 2011):
    filename = 'data/baby/yob{}.txt'.format(year)
    d1 = pd.read_csv(filename, names=['name', 'sex', 'births'])
    d1['year'] = year
    tmp.append(d1)

# 리스트에 있는 데이트 프레임 concat
data = pd.concat(tmp, ignore_index=True)
# print(data)

# 년도와 성별에 따른 출생아수
s1 = data.groupby(['year', 'sex'])['births'].sum()
# print(s1)

# 과제
# 1) 년도, 성별에 따른 출생아수 출력
p1 = pd.pivot_table(data, index='year', columns='sex', values='births', aggfunc=sum)
# print(p1)


# 2) 1의 결과를 그래프로 출력
# plt.plot(p1)
# plt.title('연도별 성별에 따른 출생아수')
# plt.legend(['여', '남'])
# plt.show()


# # 3) 연도별 남자아이의 빈도수가 높은 이름 5개 (내 버전)
# result = []
# p2 = data[data['sex']=='M']
# for i in range(1880, 2011):
#     p4 = p2[p2['year']==i].sort_values(by='births', ascending=False)
#     p4 = p4.head()
#     result.append(p4)
# result2 = pd.concat(result, ignore_index=True)
# result2 = pd.pivot_table(result2, index=['year', 'name'], values='births')
# # print(result2)


# 이름이 연도별 성별별 출생수에서 차지하는 비율(함수 이용버전)
# def calrate(x):    
#     # print(x['births'].sum())
#     x['rate'] = x['births']/x['births'].sum()
#     return x
# g1 = data.groupby(['year', 'sex'])  # => data를 일단 연도와 성별로 그룹화
# print(g1.apply(calrate))


# 연도별 성별별 빈도수가 가장 높은 이름 2개 추출(함수 이용버전)
# def gettop2(x):
#     return x.sort_values(by='births', ascending=False)[:2]
# g1 = data.groupby(['year', 'sex'])  # => data를 일단 연도와 성별로 그룹화
# top2 = g1.apply(gettop2)            # => 그룹별로 함수 적용하여 출생수 내림차순 정렬해 상위 2개 추출
# print(top2.head())


# 연도별 성별별 빈도수가 가장 높은 이름 1000개 추출(함수 이용버전)
def gettop(x):
    return x.sort_values(by='births', ascending=False)[:1000]
g1 = data.groupby(['year', 'sex'])  # => data를 일단 연도와 성별로 그룹화
top1000 = g1.apply(gettop)            # => 그룹별로 함수 적용하여 출생수 내림차순 정렬해 상위 2개 추출
# print(top1000)


# 4) 연도와 이름에 대한 전체 출생수를 피벗
top1000 = top1000.drop('year', axis=1)  # 각 컬럼을 먼저 삭제하고
top1000 = top1000.drop('sex', axis=1)
top1000 = top1000.reset_index()         # 기존 인덱스 리셋
# print(top1000)
p3 = top1000.pivot_table(index='year', columns='name', values='births')
# print(p3)


# 연도 따른 특정 이름의 추이
d1 = p3[['Leonardo', 'Brad', 'Harry', 'Rachel']]
print(d1)
plt.plot(d1)
plt.legend(d1.columns)
plt.show()

