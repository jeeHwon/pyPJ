import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 데이터 합치기
c1 = pd.read_csv('data/concat_1.csv')
c2 = pd.read_csv('data/concat_2.csv')
c3 = pd.read_csv('data/concat_3.csv')
c2['E'] = 'ee'
# print(c1)
# print(c2)
# print(c3)

# 데이터의 연결(concat : 한번에 2개 이상의 데이터프레임을 연결 )
# d1 = pd.concat([c1,c2,c3])  # 기존인덱스가 그대로 들어온다
d1 = pd.concat([c1,c2,c3], ignore_index=True)  # 기존 인덱스 무시
print(d1)
d2 = pd.concat([c1,c2,c3], ignore_index=True, join='inner')  # 공통 컬럼만 선택
print(d2)
d3 = pd.concat([c1,c2,c3], ignore_index=True, axis=1)  # x축 방향으로 결합
print(d3)

