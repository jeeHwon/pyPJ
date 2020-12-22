import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 201222 과제
data = pd.read_csv('data/accidentdata.csv')
d1 = data[data['사상자수']>=3]

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 1) 일요일 사상자수의 최대값과 최소값 출력
print('일요일 사상자수 최소값',d1[d1['요일']=='일']['사상자수'].min())
print('일요일 사상자수 최대값',d1[d1['요일']=='일']['사상자수'].max())

# 2) 일요일 교통사고 사상자수 분포를 상자그림으로
plt.boxplot(d1[d1['요일']=='일']['사상자수'])
plt.title('일요일 교통사고 사상자수')
plt.xlabel('요일')
plt.ylabel('사상자수')
plt.ylim(0, 20)
plt.show()

# 3) 요일별 교통사고 사상자수를 상자그림으로
list = ['일','월','화','수','목','금','토']
arr = []
for i in range(len(list)):
    arr.append(d1[d1['요일']=='{}'.format(list[i])]['사상자수'])
plt.boxplot(arr, labels=list)
plt.title('요일별 교통사고 사상자수')
plt.xlabel('요일')
plt.ylabel('사상자수')
plt.ylim(0, 20)
plt.show()