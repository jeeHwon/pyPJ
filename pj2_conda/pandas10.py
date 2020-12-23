import pandas as pd 
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 과제 gap.tsv 파일을 data라는 데이터프레임으로 생성
gaps = pd.read_csv(os.path.join('data', 'gap.tsv'), sep='\t')
country = gaps['country']
continent = gaps['continent']
year = gaps['year']
lifeExp = gaps['lifeExp']
df = pd.DataFrame({country.name:country, continent.name:continent, year.name:year, lifeExp.name:lifeExp})
# print(df)

# 1) 년도별 기대수명의 평균
g1 = df.groupby('year')['lifeExp'].mean()
print('연도별 기대수명 평균:\n',g1)

# 2) 기대수명의 변화를 선그래프로 출력
plt.plot(g1)
plt.title('1952-2007 기대수명 변화')
plt.xlabel('연도')
plt.ylabel('기대수명')
plt.show()

# 3) 년도별 대륙별 기대수명의 평균
g2 = df.groupby(['year', 'continent']).lifeExp.mean()
print('연도별, 대륙별 기대수명 평균:\n',g2)

# 4) result2007.csv를 활용하여 월별 도착지연 횟수를 선그래프로 출력
df2 = pd.read_csv('data/result2007.csv', header=None)
df2.columns = ['year', 'month', 'count']
df2 = df2.set_index('month')
df2 = df2.sort_index()
plt.plot(df2['count'])
plt.title('2007년 월별 도착지연')
plt.xlabel('월')
plt.ylabel('횟수')
plt.xticks(df2.index)
plt.xlim(0,13) 
plt.show()

# 소스와 그래프 이미지 캡쳐 제출