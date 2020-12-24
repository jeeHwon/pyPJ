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
# print(c1)
# print(c2)
# print(c3)

# 데이터의 연결(concat : 한번에 2개 이상의 데이터프레임을 연결 )
# data = pd.concat([c1,c2,c3])  # 기존인덱스가 그대로 들어온다
# print(data)
# data = pd.concat([c1,c2,c3], ignore_index=True) # ignore_index : 기존 인덱스를 무시해라
# print(data)

# 어떤 데이터프레임에 다른 컬럼이 있는 경우 없는 값은 NaN으로 표시
# c2['E'] = 'ee'
# print(c2)
# data = pd.concat([c1,c2,c3], ignore_index=True)
# print(data)

# 열방향 합치기
# data = pd.concat([c1,c2,c3], ignore_index=True, axis=1)
# print(data)


# # ml-m1 영화, 평점, 사용자 데이터 읽기
# movies = pd.read_csv('data/ml-1m/movies.dat', sep="::", 
#     names=['MovieID','Title','Genres'])
# print(movies)

# ratings = pd.read_csv('data/ml-1m/ratings.dat', sep="::", 
#     names=['UserID','MovieID','Rating','Timestamp'])
# print(ratings)

# users = pd.read_csv('data/ml-1m/users.dat', sep="::", 
#     names=['UserID','Gender','Age','Occupation','Zip-code'])
# print(users)


