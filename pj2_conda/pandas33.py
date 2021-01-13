import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# data = pd.read_excel('data\\시도별 전출입 인구수.xlsx')
# data = data.fillna(method='ffill')

# # print(data)
# df = data[(data['전출지별']=='서울특별시') & (data['전입지별']!='서울특별시')]
# # print(df)
# df = df.drop('전출지별', axis=1)
# # print(df)
# df = df.set_index('전입지별')
# # print(df)

# 선그래프
# plt.plot([30,20,5,10], 'o')           # y축만 출력 (x축 임의값)
# plt.plot([1,2,3,4],[30,20,5,10], 'o') # x축 지정값으로 출력
# plt.xticks([1,2,3,4])                 # x축 간격 설정
# plt.yticks([0,20,40,60])              # y축 간격 설정/
# plt.yticks(list(range(0,61,20)))      # y축 간격 설정(상동)
# plt.show()

# print(df.loc['부산광역시']) # series
# plt.style.use('bmh')
# plt.style.use('ggplot')
# plt.plot(df.loc['부산광역시'])
# plt.plot(df.loc['제주특별자치도'])
# plt.xticks(rotation='60', size=10)
# plt.xlabel('연도')
# plt.ylabel('건수')
# plt.title('연도별 서울에서 타지방으로 이사한 건수')
# plt.legend(['부산','제주'])
# plt.show()


# ===============================================
car = pd.read_csv('data\\mpg.csv', header=None)
# 행인덱스 car.index
# 열인덱스 car.columns
print(car)
print(car.index)    # RangeIndex(start=0, stop=398, step=1
print(car.columns)  # Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8], dtype='int64')
car.columns = ['mpg', 'cyn', 'disp', 'horsepower', 'weight', 'acc', 'modelyear', 'country', 'name']
print(car)
car.info()
# country 1->미국 2->유렵 3->일본
def  getCountry(x):
    if x==1:
        return '미국'
    elif x==2:
        return '유럽'
    else:
        return '일본'
car['country1'] = car['country'].apply(getCountry)
print(car)

# 연비의 box-plot & histogram
# plt.boxplot(car['mpg'])
# plt.show()
# plt.hist(car['mpg'])
# plt.show()

# 제조국별 연비의 box-plot & histogram
# print(car[car['country1']=='미국']['mpg'])
# plt.boxplot([car[car['country1']=='미국']['mpg'],
#             car[car['country1']=='유럽']['mpg'],
#             car[car['country1']=='일본']['mpg']], 
#             labels=['미국','유럽','일본'])
# plt.show()

# 미국산 자동차 연비의 histogram
# plt.hist(car[car['country1']=='미국']['mpg'])
# plt.show()

# 제조국별 자동차 수
# s1 = car.groupby('country1').count()    # 모든열의 데이터 갯수 세기
# s1 = car.groupby('country1').size()    # 레코드 수(행의 수) 세기
# plt.pie(s1, labels=s1.index, autopct='%.1f%%')
# plt.show()

# 연비와 무게 사이의 관계
# plt.scatter(car['mpg'], car['weight'])
# plt.show()
