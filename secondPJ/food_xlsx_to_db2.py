from numpy.lib.function_base import diff
import pandas as pd
import pymysql 
import sqlalchemy


df = pd.read_csv('data/total_food.csv', encoding='cp949', skiprows=2)
col_list = list(df.columns)
col_dict = {i : col_list[i] for i in range(len(col_list))}

print(col_dict)

df = df.iloc[:,[0,2,3,9,10,5,11,15,21,31,20,188,191,19,55,59,64,75,76,101,79,81,91,95,98,99,89,94,38,42,45,44,41,39,46,47]]
# 컬럼에 대한 소견
# DB군 : 가공식품 제거:  총 데이터수 47606 => 11861개
df = df[df['DB군']!='가공식품']
# 에너지(kj) : kcal를 보조하는 컬럼으로 보임. kcal로 통일하기로 함
# 수분 제외
# 총 식이섬유(mg) 0인 데이터 1개, 무시
# 한국인 영양소 섭취기준에 의거, g단위 디폴트, mg 데이터 무시
# 비타민 E(㎎) -> 비타민 E(㎎ α-TE)로 대체(pdf 기준)
# 비타민 K(㎎) 0 아닌 데이터 69개 -> 비타민 K(㎍)로 단위 전환

df.loc[(df['비타민 K(㎎)']!=0), '비타민 K(㎍)'] = df.loc[df['비타민 K(㎎)']!=0]['비타민 K(㎎)'] * 1000
df = df.drop(['비타민 K(㎎)'], axis=1)

# 티아민 = 비타민 B1(㎎)
# 리보플라빈 = 비타민 B2(㎎)
# 엽산 = folic acid
# 비타민 B12(㎎) 0 아닌 데이터 -> 비타민 B12(㎍)로 단위 전환
df.loc[(df['비타민 B12(㎎)']!=0), '비타민 B12(㎍)'] = df.loc[df['비타민 B12(㎎)']!=0]['비타민 B12(㎎)'] * 1000
df = df.drop(['비타민 B12(㎎)'], axis=1)

# 컬럼 테이블 형식에 맞게 변형
df.columns = [    
    'food_no','food_code','food_cate1','food_cate2','food_cate3','food_name','food_serving',
    'food_energy','food_carbo','food_fiber','food_lipid','food_linoleic_acid','food_a_linoleic_acid',
    'food_pro','food_vitA','food_vitD','food_vitE','food_vitK','food_vitC','food_thia',
    'food_ribo','food_vitB6','food_folic','food_vitB12','food_panto','food_bio','food_ca',
    'food_p','food_na','food_k','food_mg','food_fe','food_zn','food_cu']

# print(df.columns)
# print(df.sample(n=5))
# print(df.info())

df.loc[(df['food_cate3']=='피자류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='커피류'), 'food_cate3'] = '음료'
df.loc[(df['food_cate3']=='어류'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='차류'), 'food_cate3'] = '음료'
df.loc[(df['food_cate3']=='어패류 및 기타 수산물'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='채소류'), 'food_cate3'] = '반찬3'
df.loc[(df['food_cate3']=='케이크류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='스무디류'), 'food_cate3'] = '음료'
df.loc[(df['food_cate3']=='기타 빵류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='육류'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='곡류 및 그 제품'), 'food_cate3'] = '주식'
df.loc[(df['food_cate3']=='샌드위치류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='과실류'), 'food_cate3'] = '부식'
df.loc[(df['food_cate3']=='아이스크림류'), 'food_cate3'] = '부식'
df.loc[(df['food_cate3']=='패류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='기타'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='탄산음료류'), 'food_cate3'] = '음료'
df.loc[(df['food_cate3']=='치킨류'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='과일.채소음료류'), 'food_cate3'] = '음료'
df.loc[(df['food_cate3']=='수산가공품'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='버거류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='조리가공품류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='해조류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='빙수류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='조미료류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='페이스트리류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='기타 과자류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='도넛류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='식빵류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='버섯류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='견과류 및 종실류'), 'food_cate3'] = '부식'
df.loc[(df['food_cate3']=='쿠키.비스킷류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='샐러드'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='갑각류'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='감자 및 전분류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='채소류튀김'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='두류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='두족류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='튀김빵류(도넛, 꽈배기 등)'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='크림빵류 '), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='우유 및 유제품류'), 'food_cate3'] = '부식'
df.loc[(df['food_cate3']=='당류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='스파게티류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='크림빵류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='어패류국.탕'), 'food_cate3'] = '국물'
df.loc[(df['food_cate3']=='나물.채소류무침'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='육류구이'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='유지류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='김밥(초밥)류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='육류국.탕'), 'food_cate3'] = '국물'
df.loc[(df['food_cate3']=='채소류국.탕'), 'food_cate3'] = '국물'
df.loc[(df['food_cate3']=='주류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='앙금빵류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='난류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='기타 튀김류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='김치'), 'food_cate3'] = '반찬3'
df.loc[(df['food_cate3']=='떡류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='어패류볶음'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='음료류'), 'food_cate3'] = '음료'
df.loc[(df['food_cate3']=='어패류무침'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='나물.숙채류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='장아찌.절임류'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='어패류튀김'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='국수류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='육류볶음'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='채소류볶음'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='어패류찜'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='어패류구이'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='채소류전'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='채소류찌개.전골'), 'food_cate3'] = '국물'
df.loc[(df['food_cate3']=='덮밥류'), 'food_cate3'] = '주식'
df.loc[(df['food_cate3']=='기타 음료 및 차류'), 'food_cate3'] = '음료'
df.loc[(df['food_cate3']=='초콜릿류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='육류찌개.전골'), 'food_cate3'] = '국물'
df.loc[(df['food_cate3']=='육류튀김'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='어패류조림'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='죽류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='어패류찌개.전골'), 'food_cate3'] = '국물'
df.loc[(df['food_cate3']=='육류찜'), 'food_cate3'] = '반찬1'
df.loc[(df['food_cate3']=='한과류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='중식면류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 밥류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='리조또.그라탕류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='쌀밥.잡곡밥류'), 'food_cate3'] = '주식'
df.loc[(df['food_cate3']=='볶음밥류'), 'food_cate3'] = '특식'
df.loc[(df['food_cate3']=='우유.유제품류'), 'food_cate3'] = '부식'
df.loc[(df['food_cate3']=='스낵류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='육류조림'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='채소류조림'), 'food_cate3'] = '반찬2'
df.loc[(df['food_cate3']=='적류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='어패류전'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='만두류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='떡볶이류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='채소류찜'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='젓갈류'), 'food_cate3'] = '반찬3'
df.loc[(df['food_cate3']=='기타 국 및 탕류'), 'food_cate3'] = '국물'
df.loc[(df['food_cate3']=='비빔밥류'), 'food_cate3'] = '주식'
df.loc[(df['food_cate3']=='스프류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='라면류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='육류전'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 전.적 및 부침류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='채소류구이'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 조림류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 생채.무침류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 찜류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 볶음류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='회류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='곡류 및 서류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='냉국류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='부침류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='포류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 면 및 만두류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 아이스크림류'), 'food_cate3'] = '기타'
df.loc[(df['food_cate3']=='기타 구이류'), 'food_cate3'] = '기타'

# 인덱스 초기화 후 재설정
df.reset_index(drop=True, inplace=True)


# DB 접속
conn = None
cur = None
sql = ""
conn = pymysql.connect(host='sarte.kr', user='root', password='1234', db='food', charset='utf8')

# 테이블 생성
cur = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS food (\
    food_no int,\
    food_code char(10),\
    food_cate1 char(10),\
    food_cate2 char(30),\
    food_cate3 char(30),\
    food_name char(50),\
    food_serving double,\
    food_energy double,\
    food_carbo double,\
    food_fiber double,\
    food_lipid double,\
    food_linoleic_acid double,\
    food_a_linoleic_acid double,\
    food_pro double,\
    food_vitA double,\
    food_vitD double,\
    food_vitE double,\
    food_vitK double,\
    food_vitC double,\
    food_thia double,\
    food_ribo double,\
    food_vitB6 double,\
    food_folic double,\
    food_vitB12 double,\
    food_panto double,\
    food_bio double,\
    food_ca double,\
    food_p double,\
    food_na double,\
    food_k double,\
    food_mg double,\
    food_fe double,\
    food_zn double,\
    food_cu double\
    )"
cur.execute(sql)
conn.commit()
conn.close()


# 오류 발생하는 컬럼 데이터 수정
# df.loc[(df['food_no']==44612), 'food_name'] = '즉석밥, 잡곡밥'
# df.loc[(df['food_no']==47142), 'food_name'] = '커피, 커피가루, 설탕, 크림, 물에 탄것'

# 데이터가 11861개, error 방지 위해 1000개씩 11번 입력
# import time
# for i in range(11):
#     temp = df.iloc[i*1000:(i*1000)+999]
#     SQLALCHMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@sarte.kr:3306/food?charset=utf8'
#     engine = sqlalchemy.create_engine(SQLALCHMY_DATABASE_URI, echo=False, encoding='utf-8')
#     temp.to_sql(name='food', con=engine, if_exists='append', index=False)
#     print(f'{(i*1000)+1000}개의 데이터 입력 완료')
#     time.sleep(2)