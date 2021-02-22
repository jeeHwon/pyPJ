import pandas as pd
import pymysql 
import sqlalchemy

# 맨위에 두줄 제거
df = pd.read_csv('data/total_food.csv', encoding='cp949', skiprows=2)

# df.info() # 총 235컬럼. 최적화 위해 필요한 컬럼만 추출하여야 할듯

# 컬럼 분석은 columns_select.ipynb 참고

# 우선 가장 최소한의 컬럼만 추출하고 이후 필요한 컬럼이 있으면 따로 추가
df = df.iloc[:,[2,3,4,5,7,9,10,11,12,13,14,15,16,19,20,21]]
# print(df.columns)   # 선택된 컬럼 출력
# print(df.head())    # 샘플 출력

# DB 접속
conn = None
cur = None
sql = ""
conn = pymysql.connect(host='sarte.kr', user='root', password='1234', db='food', charset='utf8')

# 테이블 생성
cur = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS food_all (\
    식품코드 char(10),\
    DB군 char(10),\
    상용제품 char(15),\
    식품명 char(30),\
    지역_제조사 char(30),\
    식품대분류 char(15),\
    식품상세분류 char(15),\
    1회제공량 double,\
    내용량_단위 char(4),\
    총내용량_g double,\
    총내용량_mL double,\
    에너지_㎉ double,\
    에너지_kj double,\
    단백질_g double,\
    지방_g double,\
    탄수화물_g double\
    )"
cur.execute(sql)
conn.commit()
conn.close()

# 컬럼 테이블 형식에 맞게 변형
df.columns = ['식품코드', 'DB군', '상용제품', '식품명', '지역_제조사', '식품대분류', '식품상세분류', '1회제공량', '내용량_단위',\
    '총내용량_g', '총내용량_mL', '에너지_㎉', '에너지_kj', '단백질_g', '지방_g', '탄수화물_g']
df = df.fillna(0)
# print(df.isnull().sum())

# 일부(1000개)만 추출
df = df.loc[:1000]
print(df)

# DB에 insert
SQLALCHMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@sarte.kr:3306/food?charset=utf8'
engine = sqlalchemy.create_engine(SQLALCHMY_DATABASE_URI, echo=False, encoding='utf-8')
df.to_sql(name='food_all', con=engine, if_exists='append', index=False)