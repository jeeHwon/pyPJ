import pandas as pd
from pandas.core.accessor import PandasDelegate
from pandas.core.frame import DataFrame 
import seaborn as sns

# 과제
# 1)2007년 출발지연 데이터 집계데이터를 데이터프레임으로 변환하시오
# 2)월을 인덱스로 지정하세요
# 3)3월부터 6월까지의 데이터를 출력하세요
# 4)데이터프레임과 시리즈를 비교하세요

# 1) 데이터프레임 변환
df = pd.read_csv('data/result2007.csv', header=None)

# 2) 월을 인덱스로 지정
df.columns = ['year', 'month', 'count']
df = df.set_index('month')

# 3) 3월부터 6월까지 데이터 출력
print(df.loc[3:6])

# 4) 데이터프레임과 시리즈 비교
# - Pandas
# 데이터 분석 위한 도구로 자료구조 및 그에대한 분석 기능을 제공하는 패키지

# - Series 
# 판다스 주요 자료 구조로서 인덱스와 그에 대한 데이터로 이루어진 구성

# - DataFrame
# 행(index), 열(columns), 값(values)로 이루어져 여러개의 시리즈가 결합된 형태