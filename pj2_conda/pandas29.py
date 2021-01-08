import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

data =  pd.read_csv('data\\mpg.csv', header=None)
data.columns = ['mpg','cyl','displace','horsepower','weight','acc','modelyear','country','name']
# print(data)

# ==원그래프 
# 방법 )1 
# s1 = data.groupby('country').size()
# print(s1, type(s1))
# s1.index = ['미국','유럽','일본']
# print(s1)
# plt.style.use('ggplot')
# plt.pie(s1, labels=s1.index, colors=['steelblue','indigo','limegreen'], autopct='%.2f%%')
# plt.title('자동차 생산국')
# plt.show()

# d1 = data[['weight','acc','modelyear','country','name']]
# d1.info()
# print(d1.sum())
# print(d1.mean())    # 수치형 자료만 계산

# 방법 )2 
# data['cnt'] = 1
# print(data)
# df1 = data.groupby('country').sum()
# df1.index = ['미국','유럽','일본']
# # print(df1)
# plt.pie(df1['cnt'])
# plt.show()

# ==히스토그램
# plt.hist(data['mpg'], bins=20, color='red')
# plt.title('연비 histogram')
# plt.show()

# == Boxplot
# 연비의 boxplot
# plt.boxplot(data['mpg'], vert=False)
# plt.show()
# 나라별 연비의 boxplot
# print(data[data['country']==1]['mpg'])
# print(data[data['country']==2]['mpg'])
# print(data[data['country']==3]['mpg'])
# plt.boxplot([data[data['country']==1]['mpg'],
#     data[data['country']==2]['mpg'],
#     data[data['country']==3]['mpg']], labels=['미국','유럽','일본'])
# plt.show()

# == 산점도
# 자동자 무게와 연비와의 관계
# plt.scatter(data['weight'],data['mpg'])
# plt.scatter(data['weight'],data['mpg'], s=data['cyl']*20, c='orange',alpha=0.5) # 점 크기로 실린더 구분
# plt.scatter(data['weight'],data['mpg'], c=data['cyl'])                          # 색으로 실린더 구분
# plt.title('자동차 무게와 연비의 산점도')
# plt.show()

import seaborn as sns
def getSex1(x):
    if x=='Female':
        return 0
    else:
        return 1

tips = sns.load_dataset('tips')
tips['sex2'] = tips['sex'].apply(getSex1)
# print(tips)
# plt.scatter(tips[tips['sex2']==0]['total_bill'], tips['tip'], s=tips['size']*15, c=tips['sex2'], label=['남','여'])
# plt.scatter(tips[tips['sex2']==1]['total_bill'], tips['tip'], s=tips['size']*15, c=tips['sex2'], label=['남','여'])
plt.scatter(tips[tips['sex2']==0]['total_bill'], tips[tips['sex2']==0]['tip'], s=tips['size']*15, color='red', label='여', alpha=0.5)
# plt.scatter(tips[tips['sex2']==1]['total_bill'], tips[tips['sex2']==1]['tip'], s=tips['size']*15, color='blue', label='남', alpha=0.5)
plt.legend()
plt.show()

