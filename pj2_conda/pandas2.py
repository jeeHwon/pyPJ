import pandas as pd 
import seaborn as sns
# tips = sns.load_dataset('tips')
# print(tips)

# print(tips.head())                # 앞에서 5개 출력(기본)
# print(tips.head(n))               # 앞에서 n개 출력
# print(tips.tail())                # 뒤에서 5개 출력(기본)
# print(tips.tail(n))               # 뒤에서 n개 출력

# ==Dataframe 기본
# print(type(tips))                 # 타입은 데이터프레임(2차원)
# print(tips.shape)                 # (244, 7) 튜플 형태로 반환 ->행과 열의 크기
# print(tips.shape[0])              # 행의 수
# print(tips.shape[1])              # 열의 수
# print(tips.columns)               # 열 이름
# print(tips.dtypes)                # 각 열의 데이터 타입
# tips.info()                       # 전체 정보를 출력 (print 안줘도)

# print(tips['total_bill'])         # 열 이름으로 전체출력
# print(type(tips['total_bill']))   # 타입은 시리즈(1차원)

# smoker = tips['smoker']
# print(type(smoker))               # 변수로 지정해도 시리즈

# loc : 인덱스를 기준으로 행데이터 추출
# iloc : 행번호를 기준으로 행데이터 추출, 판다스에서 행번호 부여
# r240 = tips.loc[240]              # 240번째 행 출력
# print(r240)
# print(type(r240))                 # 역시 시리즈
# print(tips.loc[[10, 20, 30]])
# print(tips.iloc[[10, 20, 30]])
# print(tips.loc[243])    # -1로 접근못해 왜? 인덱스에 -1이 없잖아
# print(tips.iloc[-1])    # -1로 맨 마지막으로 접근 가능

# print(tips[['total_bill', 'smoker']])         # 두개 이상의 열로 출력 할 땐 [[]]로 접근
# print(type(tips[['total_bill', 'smoker']]))   # 타입은 데이터프레임(2차원)

# ==인덱스 변경
# t1 = tips.set_index('total_bill')   # index를 다른 열로 셋팅
# print(t1)
# t1 = t1.reset_index()               # 기존 인덱스를 열로, 새로운 인덱스열 생성
# print(t1)

# ==행 접근 방법
# loc로 접근
# print(range(10, 50, 10))
# print(list(range(10, 50, 10)))
# t1 = tips.loc[:, ['total_bill', 'tip']]     #데이터 프레임[행, 열] loc는 컬럼명으로 접근가능
# print(t1)
# print(tips.loc[:10, ['tip','day']])

# iloc로 접근
# t1 = tips.iloc[:, ['total_bill', 'tip']]     #에러 발생           iloc는 모두 보이지 않는 숫자로 접근해야함
# print(t1)
# t1 = tips.iloc[:, [2, 3, 6]]  이렇게 index로 자유롭게 접근가능
# print(t1)
# print(tips.iloc[list(range(10, 50, 2)), [0, 1]])



# movies = pd.read_csv('data/mov.csv', header=None) # header 없을때
movies = pd.read_csv('data/mov.csv')              # header 있을때
# print(movies['title'])
# print(movies.loc[0])
# print(movies[['title', 'star']])
m1 = movies.set_index('title')
# print(m1)
# print(m1['star'])
m1 = m1.reset_index()
# print(m1)
# print(m1.loc[0])    # 인덱스 중 0을 찾아 출력
# print(m1.iloc[0])   # 데이터 중 0번째 행을 출력