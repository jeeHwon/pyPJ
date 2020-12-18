from os import sep
import pandas as pd
import seaborn as sns
tips = sns.load_dataset('tips')
# print(tips)
movies = pd.read_csv('data/mov.csv')
# print(movies)

data = pd.read_csv('data/gap.tsv', sep='\t')

# country 컬럼을 선택
# 컬럼의 값과 조건을 비교
# 그 결과를 새로운 변수에 할당
is_venezuela = data['country'] == 'Korea'

# 조건를 충족하는 데이터를 필터링하여 새로운 변수에 저장
venezuela = data[is_venezuela]

# 결과를 출력
print(venezuela)