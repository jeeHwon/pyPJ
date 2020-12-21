import pandas as pd 
import seaborn as sns 
import os

# tips = sns.load_dataset('tips')
# print(tips)
# tips.info()

# print(type(tips))
# print(tips['time'])
# print(tips['time'])
# print(type(tips['time']))
# print(type(tips.loc[3]))

# 데이터 하나에 접근
# print(tips.iloc[1]['tip'])

# 데이터 여러개 접근
# print(tips.loc[:3,['total_bill','tip']])
# print(tips.iloc[:3,:2])

# index 변경
# print(tips)
# tips = tips.set_index('day')    # 기존 인덱스 삭제, 지정될 열이 새로운 인덱스로 변경
# print(tips)
# print(tips.loc['Sun'])          # 인덱스 중복되어 여러건이 나온다
# tips = tips.set_index('smoker') # 요일 컬럼 삭제되고 스모커 인덱스로 대체
# print(tips)
# tips = tips.reset_index()       # 기존 인덱스를 열이 되고 새로운 일련번호 부여
# print(tips)                     # 이미 없어진 요일은 어쩔수없어..

# s1 = pd.Series(['rose', 'iris', 'cosmos'])
# print(s1)
# print(type(s1))
# s2 = pd.Series(['오대수', '서울', '43세', '수줍음'], index=['이름', '주소', '나이', '성격'])
# print(s2[1])

# movies = pd.read_csv(os.path.join('data', 'mov.csv'))
# movies = pd.read_csv(os.path.join('data', 'mov.csv'), header=None, names=['영화제목', '평점','예매율'])
# print(movies)
# print(movies.columns)
# movie10 = movies.head(10)
# print(movie10)
# print(movie10.loc[1])       # 인덱스 값으로 접근
# print(movie10.iloc[1])      # 행번호 값으로 접근
# print(movie10.loc[3:5])
# print(movie10.iloc[3:5])
# print(movie10.iloc[[1,3,5]])
# movie10 = movie10.set_index('title')
# print(movie10.loc[['조제','이웃사촌'],['star']])
# print(movie10.iloc[[0,1],[0]])

# 데이터 프레임 생성
# person = pd.DataFrame({
#     'name':['간디', '나폴레옹', '미야자키하야오', '디카프리오'],
#     'addr': ['인도', '프랑스','일본','미국'],
#     'age': [87, 123, 56, 48],
#     'hobby': ['복싱', '동양화', '골프', '국궁']},
#     columns=['addr','age','hobby','name'] # 컬럼 순서 지정 가능
# )
# print(person)
# s1 = person['name']
# print(type(s1))         # 타입 : Series
# print(s1)

# Series의 속성 1)index 2)values 로 이루어짐
# print(s1.index)
# print(s1.values)

# Series의 메서드 
# print(s1.keys())    # == s1.index
# print(s1.index[0])
# print(s1.keys()[0])
# print(person['age'].mean())        # 평균값 : 78.5
# print(person['age'].max())         # 최대값 : 123
# print(person['age'].min())         # 최소값 : 48
# print(person['age'].std())         # 표준편차 : 34.10..
# print(person['age'].sum())         # 합 : 314

# 불린 추출
# ages = person['age']
# print(ages)
# print(ages.mean())
# print(ages>ages.mean())     # True, True, False, False
# print('참인것만 출력:',ages[[True,True,False,False]])
# print('나이 평균 이상 출력:',ages[ages>ages.mean()])

tips = sns.load_dataset('tips')
# tips10 = tips.tail(10)
# print(tips10)
# s1 = tips10['tip']
# print('팁의 평균:\n', s1.mean())
# print('팁의 평균 이상 여부:\n', s1>s1.mean())
# print('팁의 평균 이상 데이터 출력:\n', s1[s1>s1.mean()])

# 브로드캐스팅 : 시리즈나 데이터프레임에 있는 모든 데이터에 대해 한번에 연산
# 벡터 : 여러개의 값을 가진 데이터
# print(s1+s1)    # 벡터끼리 연산 (같은 인덱스끼리)
# print(s1*s1)    # 벡터끼리 연산
# print(s1+1000)   # 모든 벡터에 1000이 더해짐
# s2 = pd.Series([1,2,3,4,5])
# print(s1)
# print(s2)
# print(s1+s2)    # NaN 인덱스가 달라서 연산 오류
# s1.index = range(0, 10, 1)
# print(s1+s2)    # 길이가 다른 벡터 연산

# 정렬
# s3 = tips['total_bill'].head(10)
# print(s3)
# print(s3.index)
# print('인덱스 순서 정렬\n',s3.sort_index())
# print('인덱스 순서 역순정렬\n',s3.sort_index(ascending=False))
# print(s3.values)
# print('값 순서 정렬\n',s3.sort_values())                    
# print('값 순서 역순정렬\n',s3.sort_values(ascending=False)) 

#샘플데이터
tips2 = tips.sample(n=10, random_state=19)   # 19를 주면 19를 준 데이터는 모두 같음
tips2 = tips2.set_index('day')
# print(tips2)
# print(tips2.sort_values(by='total_bill'))
# print(tips2.sort_values(by='smoker'))
# print(tips2.sort_values(by=['total_bill','smoker']))
# print(tips2.sort_index())

# 컬럼 추가
# tips2['tot'] = tips2['total_bill']+tips2['tip']
# print(tips2)

# 컬럼 삭제
# tips2 = tips2.drop('sex', axis=1)
# print(tips2)

# 데이터 프레임 저장
# tips2.to_csv('data\\tips2.csv')
# tips2.to_pickle('data\\tips2.pickle')


