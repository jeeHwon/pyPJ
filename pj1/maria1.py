import pymysql
# 데이터 출력----------------------------------------------------------
# 1) 데이터 베이스 연결
conn = pymysql.connect(host='localhost', port=3307, user='root', password='asdf1038', db='pythondb', charset='utf8')

# 2) 커서 생성
# cur = conn.cursor() # 튜플로 반환
cur = conn.cursor(pymysql.cursors.DictCursor) # 딕셔너리로 반환

# 3) 쿼리생성
sql = 'select * from member'

# 4) 실행처리
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    # print(row)
    print(row['no'], row['name'],row['age'],row['email'],row['birthyear'])


# 데이터 입력----------------------------------------------------------
# 1) 데이터 베이스 연결
conn = pymysql.connect(host='localhost', port=3307, user='root', password='asdf1038', db='pythondb', charset='utf8')

# 2) 커서 생성
# cur = conn.cursor() # 튜플로 반환
cur = conn.cursor(pymysql.cursors.DictCursor) # 딕셔너리로 반환

# 3) 쿼리생성
while(True):
    name=input('사용자 이름 : ')
    if name == "":
        break
    age=input('사용자 나이 : ')
    email=input('사용자 이메일 : ')
    birthyear=input('사용자 태어난년도 : ')
    sql = 'insert into member (name, age, email, birthyear) values (%s, %s, %s, %s)'
    # 4) 실행처리
    cur.execute(sql,(name, age, email, birthyear))

# 4-1) 데이터 출력
sql = 'select * from member'
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    # print(row)
    print(row['no'], row['name'],row['age'],row['email'],row['birthyear'])
conn.commit()

# 5) 자원해제
conn.close()


# 데이터 삭제----------------------------------------------------------
# conn = pymysql.connect(host='localhost', port=3307, user='root', password='asdf1038', db='pythondb', charset='utf8')
# cur = conn.cursor(pymysql.cursors.DictCursor) 
# age = input('나이 =')
# sql = 'delete from member where age <= %s'
# cur.execute(sql,(age,)) #tuple 임을 알려주기 위해 하나 있어도 commma 찍자
# conn.commit()
# conn.close()

# 이름과 태어난 년도를 입력바당 이름, 나이, 태어난 년도를 수정
# 데이터 수정----------------------------------------------------------
conn = pymysql.connect(host='localhost', port=3307, user='root', password='asdf1038', db='pythondb', charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor) 
name = input('이름 : ')
birthyear = input('태어난 년도 : ')
age = 2020 - int(birthyear) +1

sql = "update member set age = %s where name = %s"
cur.execute(sql,(age,name))
sql = "update member set birthyear = %s where name = %s"
cur.execute(sql,(birthyear,name)) 
conn.commit()
conn.close()
