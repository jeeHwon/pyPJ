import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import font_manager, rc
import json

fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# data = {'k1':['a','b','b','c','c'],
#         'k2':['v','w','w','x','y'],
#         'data':[1,2,3,4,5]
#         }

# df = pd.DataFrame(data)
# print(df)

# 중복데이터 확인
# print(df.duplicated(['k1']))
# print(df.duplicated(['k1','k2']))

# 중복데이터 제거
# print(df.drop_duplicates(['k1']))                # default로 앞에꺼 살리고 뒤에꺼 제거
# print(df.drop_duplicates(['k1'], keep='last'))   # 앞에꺼 제거하고 마지막꺼를 살려
# print(df.drop_duplicates)                        # 완전히 동일한 데이터만 삭제(모든 열의 값이 동일)

food = json.load(open('data\\food.json'))
# print(food)
# print(type(food))   # 리스트
# print(len(food))    # 6636
# print(food[0])
# print(food[0].keys())
# print(food[0]['nutrients'])
# n1 = pd.DataFrame(food[0]['nutrients'])
# print(n1)

# 음식정보만 따로 데이터프레임으로 생성
info = pd.DataFrame(food, columns=['id','group','description'])
# print(info)

# 영양소 정보 데이터만을 추출해 데이터프레임 생성
temp = []
for dic in food:
    nut = pd.DataFrame(dic['nutrients'])
    nut['id'] = dic['id']
    temp.append(nut)
data = pd.concat(temp, ignore_index=True)
data = data.drop_duplicates()
# print(data.shape)

# 컬럼명 변경 - 1) 전체수정
# info.columns=['foodid', 'foodgroup', 'foodname']
# print(info)

# 컬럼명 변경 - 2) 부분수정
info = info.rename(columns={'group':'foodgroup', 'description' : 'foodname'})

# 두 데이터프레임 병합
df = info.merge(data, on='id')
df.info()
# print(df.groupby(['foodgroup','group'])['value'].mean())