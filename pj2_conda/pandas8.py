import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

tips = sns.load_dataset('tips')
# print(tips)
# 요일별 식대의 집계
# print(tips.groupby('day')['total_bill'].mean())

# 10개 데이터 임의 추출
# tips10 = tips.sample(10, random_state=42)
# print(tips10)

# 그룹객체의 속성
# g1 = tips10.groupby('sex')
# print(g1.groups)

# 그룹객체의 메서드
# print(g1.get_group('Female'))           # 특정 그룹 추출
# for data in g1:
#     print(data)
#     print(type(data))                   # 튜플 형태 (group, data)
#     print(len(data))                    # 길이 : 2
#     print(type(data[0]), type(data[1])) # <class 'str'> <class 'pandas.core.frame.DataFrame'>

# 성별별 식대의 평균
# g1 = tips.groupby('sex')['total_bill'].mean() 
# g1 = tips.groupby('sex').total_bill.mean()  # 위코드와 동일한 결과
# print(g1)

# 성별별 식사시간의 식대평균
# g2 = tips.groupby(['sex', 'time']).total_bill.mean()
# print(g2)
# print(type(g2)) # 타입 : 시리즈
# print(g2.index)
# print(g2.values)
# print(g2.sort_values())
# d2 = g2.reset_index()   # 기존 인덱스를 일반컬럼으로 추가하고 새로운 인덱스 부여
# print(d2)
# print(type(d2)) # 타입 : 데이터프레임

# 교통사고 데이터 불러오기(사상자수 3명 이상)
data = pd.read_csv('data/accidentdata.csv')
# print(data)

# 요일별 교통사고 사상자 합계 구하기
# d1 = data[data['사상자수']>=3]
# print(d1)
# g1 = d1.groupby('요일')['사상자수'].sum()
# print(g1)   
# print(type(g1)) # 타입: 시리즈  

# plt.plot(g1)
# plt.title('2012-2014 요일별 교통사고 사상자수 합')
# plt.xlabel('요일')
# plt.ylabel('사상자수')
# plt.show()

# 인덱스 순서 변경(현재 가나다순 -> 금 목 수 월 일 토 화)
# g1 = g1.reindex(['월','화','수','목','금','토','일'])
# plt.plot(g1)
# plt.title('2012-2014 요일별 교통사고 사상자수 합')
# plt.xlabel('요일')
# plt.ylabel('사상자수')
# plt.show()

# 시리즈를 데이터프레임으로 변경
# d2 = g1.reset_index()
# print(d2)
# plt.plot(d2['요일'], d2['사상자수'])
# plt.show()

# 경기도내 교통사망사고가 높은 5개 지역 분석하여 도식화
# print(data)
# -점그래프
# d2 = data[data['발생지시도']=='경기']
# print(d2.iloc[0])
# g2 = d2.groupby('발생지시군구')['사망자수'].sum()
# g2 = g2.sort_values(ascending=False).head(5)
# plt.plot(g2.index, g2.values,'o')
# plt.show()

#-원그래프
# plt.pie(g2, 
#     labels=g2.index, 
#     colors=['red', 'orange', 'yellow', 'green', 'blue'],
#     autopct='%.2f%%')
# plt.title('2012-2014 경기도 교통사망사고 높은 지역')
# plt.show()

# import numpy as np 
# df = tips.head(30)
# print(df)
# df['sex'] = "A"+df['sex']
# buylist = df['sex'].values.tolist()

# print(buylist)
code1 = 123456
code2 = 567861
rows = []
rows.append('A'+str(code1))
rows.append('A'+str(code2))
print(rows)