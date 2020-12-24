import pandas as pd 
from numpy import NaN, nan, NAN

# 과제
#1) 아이티 지진시 휴대폰으로 응급사항등에 대한 전화내역 파일인
# h.csv를 읽어 데이터프레임생성,자료의 행과 열확인,자료형 확인
df = pd.read_csv('data/h.csv')
print(df.columns)
print(df.index)
df.info()

# 2)메시지종류(CATEGORY)컬럼 10줄 확인
print(df['CATEGORY'].head(10))

# 3)CATEGORY가 널인 자료 제거,자료의 행과 열확인
# print(df.shape[0]-df.count())
df2 = df[df['CATEGORY'].notnull()]
print(df2)

# 4)위치정보가 잘못된 자료 제거,자료의 행과 열확인
# 유효한 위치 : 18<LATITUDE<20, -75<LONGITUDE<-70
df3 = df[(df['LATITUDE']>18)& (df['LATITUDE']<20)]
df3 = df3[(df3['LONGITUDE']>-75) & (df3['LONGITUDE']<-70)]
print(df3)