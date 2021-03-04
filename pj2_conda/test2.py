# 탐색적 데이터 분석
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프처리 및 파일 로드
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 1)
data = pd.read_csv('data/rtest.csv')
# print(data.dtypes)
# print(data.shape)

# 2)
def getResident2(x):
    if x == 1:
        return '서울'
    elif x == 2:
        return '인천'
    elif x == 3:
        return '대전'
    elif x == 4:
        return '대구'
    else:
        return '시군구'
data['resident2'] = data['resident'].apply(getResident2)
# print(data.head())

# 3)
# print(data.shape)
data = data[data['age'].notnull()]
# print(data.shape)

# 4)
# print(data['age'].min())
# print(data['age'].max())
# print(data['age'].mean())

# 5)
# plt.boxplot(data['age'])
# plt.title('연령대')
# plt.show()

# 6)
def getAge2(x):
    if x<=30:
        return '청년층'
    elif 31<=x<=55:
        return '중년층'
    elif x>=56:
        return '장년층'

data['age2'] = data['age'].apply(getAge2)
print(data.head())

# 7)
def getGender2(x):
    if x == 1:
        return '남자'
    elif x == 2:
        return '여자'

data['gender2'] = data['gender'].apply(getGender2)
print(data.head())

# 8)
s1 = data.groupby('gender2').size()
print(s1)

# 9)
plt.pie(s1, labels=s1.index)
plt.title('남녀의 빈도수')
plt.show()

# 10)
plt.scatter(data['age'], data['price'])
plt.show()
