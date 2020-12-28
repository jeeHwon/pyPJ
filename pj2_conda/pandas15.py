import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

df = pd.read_csv('data/ebola.csv')
# print(df)
# df.info()

# print(df.shape)
# print('값의 갯수\n', df.count())
# print('누락된 값의 갯수\n', df.shape[0]-df.count())
# e1 = df.iloc[:10, :5]
# print(e1)

# 누락값 처리
# print('지정값으로 변경\n', e1.fillna(0))
# print('누락값 양쪽에 있는 값의 평균으로 변경\n', e1.interpolate())
# print('누락값이 포함된 행 삭제\n', e1.dropna())
# print('누락값 전의 값으로 변경\n', e1.fillna(method='ffill'))
# print('누락값 후의 값으로 변경\n', e1.fillna(method='bfill'))
# e1['tot'] = e1['Cases_Guinea']+e1['Cases_Liberia']+e1['Cases_SierraLeone']
# print(e1)
# e1['tot'] = e1['Cases_Guinea'].fillna(0)+e1['Cases_Liberia'].fillna(0)+e1['Cases_SierraLeone'].fillna(0)
# print(e1)
# print(e1.Cases_Guinea.sum())                # 기본 sum()에서 결측치 무시
# print(e1.Cases_Guinea.sum(skipna=False))    # skipna=False 옵션주면 결측치 있는 경우 nan 반환


# 피벗테이블
# 딕셔너리 의한 데이터프레임 기본 형태 => data = pd.DataFrame({key1:[], key2:[], key3:[]})
# data = {
#     "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천" ],
#     "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010" ],
#     "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 2632035],
#     "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
# }
# data = pd.DataFrame(data)
# print(data)

# 피벗 테이블 기본구조 =>pivot(행인덱스로 사용할 열, 열인덱스로 사용할 열, 데이터로 사용할 열)
# p1 = data.pivot('도시', '연도', '인구')
# print(p1)
# print(type(p1))
# print(p1.index)
# print(p1.columns)
# p2 = data.pivot_table(index=['도시', '연도'], values='인구')
# print(p2)
# data2 = pd.read_excel('data/판매현황.xlsx')
# p2 = pd.pivot_table(data2, index='분류', values='판매수량')
# print(p2)   # 기본 aggfunc를 지정하지 않으면 평균을 구함
# p2 = pd.pivot_table(data2, index='분류', values='판매수량', aggfunc=sum) 
# print(p2)

# data2 = pd.read_excel('data\\판매현황.xlsx')
# print(data2)
# p2 = pd.pivot(data2, '분류', '상품명', '판매수량')
# p2 = pd.pivot_table(data2, index = '분류', columns = '상품명', values = '판매수량')
# print(p2)
# p3 = pd.pivot(data2, index = ['분류', '상품명'], values = '판매수량')
# p3 = pd.pivot_table(data2, index = ['분류', '상품명'], values = '판매수량')
# p3 = pd.pivot(data2, index = ['분류', '상품명'], columns = '상품코드', values = '판매수량')
# print('pivot()함수\n', p3)
# p3 = pd.pivot_table(data2, index = ['분류', '상품명'], columns = '상품코드', values = '판매수량')
# print('pivot_table()함수\n', p3)


# 교통사고
# data = pd.read_csv('data/accidentdata.csv')
# # print(data)
# # 요일별 발생지 시도별 교통사고 사망자 분석
# # print(data.columns)
# p1 = pd.pivot_table(data, index='요일', columns='발생지시도', values='사망자수', aggfunc=sum)
# # print(p1)
# p1 = p1.reindex(['월', '화', '수', '목', '금', '토', '일'])
# # print(p1)
# plt.plot(p1)
# plt.legend(p1.columns)
# plt.show()


# 영화제목별 평점 건수
# data = pd.read_csv('data/mov2.csv')
# # print(data)
# titlecnt = data.groupby('Title')['Rating'].size()
# # print(titlecnt)
# # 평점건수가 200건 이상 있는 영화 정보
# r200 = titlecnt[titlecnt>=200] # 평점건수가 200건 이상인 영화 타이틀을 r200에 저장
# # print(r200)
# data = data.set_index('Title')
# # print(data)
# data200 = data.loc[r200.index]  # 전체 데이터에서 인덱스가 r200 영화 타이틀
# # print(data200)
# data200 = data200.reset_index()
# # print(data200)

# 영화별 평균 평점
# print(data200.groupby('Title')['Rating'].mean())

# 성별에 따른 평균 평점
# print(data200.groupby(['Title', 'Gender'])['Rating'].mean())

# 성별에 따른 영화 평점
# p1 = pd.pivot_table(data200, index='Title', columns='Gender', values='Rating')

# 남자들이 좋아하는 영화
# print(p1.sort_values(by='M', ascending=False).head())
# 여자들이 좋아하는 영화
# print(p1.sort_values(by='F', ascending=False).head())
# 남녀간 호불호 갈리는 영화 10개
# p1['diff']=(p1['F']-p1['M']).abs()
# print(p1)
# print(p1.sort_values(by='diff',ascending=False).head(10))

# 호불호가 갈리는 영화 10개
# g2 = data200.groupby('Title')['Rating'].std()
# print('영화별 평점의 표준편차\n', g2)
# print(g2.sort_values(ascending=False).head(10))