import pandas as pd 
import seaborn as sns 
import os

# gap.tsv를 읽어 데이터 프레임으로 변경

# 1)g1에  country,continent,year,lifeExp 컬럼만 추출하여 데이터 프레임으로 만들세요
gaps = pd.read_csv(os.path.join('data', 'gap.tsv'), sep='\t')
country = gaps['country']
continent = gaps['continent']
year = gaps['year']
lifeExp = gaps['lifeExp']
g1 = pd.DataFrame({country.name:country, continent.name:continent, year.name:year, lifeExp.name:lifeExp})
# print(g1)

# 2)g1의 열과 행의 갯수를 조회하세요
# g1.info()           # 전체정보
# print(g1.shape)     # 튜플형태
print('g1 행의 수:',g1.shape[0])  # 행의 수
print('g1 열의 수:',g1.shape[1])  # 열의 수

# 3)lifeExp 컬럼을 기준으로 내림차순 정렬하세요
print('lifeExp 순서정렬\n',g1.sort_values(by='lifeExp', ascending=False)) 

# 4)lifeExp 열을 시리즈 s1으로 생성하세요
s1 = g1['lifeExp']
print('s1의 타입:',type(s1))

# 5)s1의 전체 평균 출력
print('s1 전체평균:',s1.mean())

# 6)s1가 40미만인것만 출력 
print('s1 중 40미만:\n', s1[s1<40])