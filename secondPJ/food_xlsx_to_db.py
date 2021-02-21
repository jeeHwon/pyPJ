import pandas as pd
import pymysql 
import sqlalchemy

# 맨위에 두줄 제거
df = pd.read_csv('data/total_food.csv', encoding='cp949', skiprows=2)


df.info() # 총 235컬럼. 최적화 위해 필요한 컬럼만 추출하여야 할듯

# 컬럼 분석은 columns_select.ipynb 참고

# 우선 가장 최소한의 컬럼만 추출하고 이후 필요한 컬럼이 있으면 따로 추가
df = df.iloc[:,[2,3,4,5,7,9,10,11,12,13,14,15,16,19,20,21]]
print(df.columns)   # 선택된 컬럼 출력
# print(df.head())    # 샘플 출력
test = df.head()
# print(test)
# SQLALCHMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@sarte.kr:3306/food?charset=utf8'
# engine = sqlalchemy.create_engine(SQLALCHMY_DATABASE_URI, echo=False, encoding='utf-8')

# test.to_sql(name='test', con=engine, if_exists='append', index=False)


# import pymysql as my

# conn = my.connect(host='sarte.kr', port=3306, user='root', password='1234', db='food', charset='utf8')
# cur = conn.cursor()
# sql = "insert into test (식품코드) values ({})"
# cur.execute(sql.format('test1'))
# conn.commit()
# conn.close()

conn = None
cur = None
sql = ""
conn = pymysql.connect(host='sarte.kr', user='root', password='1234', db='food', charset='utf8')

test.columns = ['식품코드', 'DB군', '상용제품', '식품명', '지역_제조사', '식품대분류', '식품상세분류', '1회제공량', '내용량_단위',\
    '총내용량_g', '총내용량_mL', '에너지_㎉', '에너지_kj', '단백질_g', '지방_g', '탄수화물_g']
print(test.info())
cur = conn.cursor()
# sql = "CREATE TABLE test3 (\
#     식품코드 char(10),\
#     DB군 char(10),\
#     상용제품 char(15),\
#     식품명 char(30),\
#     지역_제조사 char(30),\
#     식품대분류 char(15),\
#     식품상세분류 char(15),\
#     1회제공량 double,\
#     내용량_단위 char(4),\
#     총내용량_g double,\
#     총내용량_mL double,\
#     에너지_㎉ double,\
#     에너지_kj double,\
#     단백질_g double,\
#     지방_g double,\
#     탄수화물_g double\
#     )"
# cur.execute(sql)
# conn.commit()
# conn.close()

# cur = conn.cursor()
# sql = "insert into test3 (식품코드, DB군) values ('{}', '{}')"
# cur.execute(sql.format('test1', 'dfksdf'))
# conn.commit()
# conn.close()

# SQLALCHMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@sarte.kr:3306/food?charset=utf8'
# engine = sqlalchemy.create_engine(SQLALCHMY_DATABASE_URI, echo=False, encoding='utf-8')


# test.to_sql(name='test3', con=engine, if_exists='append', index=False)