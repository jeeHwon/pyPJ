# sqlite 실행
# .open : 데이터베이스 이름(있으면 열고, 없으면 만든다)
# .open pythondb
# .table : 현재 데이터베이스 테이블 목록
# .schema 테이블이름 :테이블 구조 확인
# .header on : select 사용시 헤더 출력
# .mode column : select 사용시 컬럼 모드로 출력
# .quit 종료

# 재 실행시
# sqlite3
# .open pythondb
# .table

import sqlite3
# 데이터베이스에서 값받아 출력하기
# 1) 데이터베이스 연결
con = sqlite3.connect('d:\\sqlite\\pythondb')
# 2) 커서생성
cur = con.cursor()
# 3) 쿼리 생성
sql = 'select * from member'
# 4) 실행 처리
cur.execute(sql)
# row = cur.fetchall()
while (True):
    row = cur.fetchone()
    if row==None :
        break
    print(list(row))
# 5) 자원해제
con.close()
print('-'*30)

# # 데이터베이스에 입력하기
# # 1) 데이터베이스 연결
# con = sqlite3.connect('d:\\sqlite\\pythondb')
# # 2) 커서생성
# cur = con.cursor()
# while (True):
#     id = input('사용자 ID= ')
#     if id=='':
#         break
#     name = input('사용자 이름= ')
#     age = input('사용자 나이= ')
#     email = input('사용자 이메일= ')
#     birthyear = input('사용자 태어난 연도= ')
#     # 3) 쿼리 생성
#     sql = "insert into member values ('{}', '{}', {}, '{}', {});".format(id, name, age, email, birthyear)
#     print(sql)
#     # 4) 실행 처리
#     cur.execute(sql)
# con.commit()
# con.close()

# member 데이터 전부삭제
# 1) 데이터베이스 연결
con = sqlite3.connect('d:\\sqlite\\pythondb')
# 2) 커서생성
cur = con.cursor()
# 3) 쿼리 생성
sql = 'delete from member'
# 4) 실행 처리
cur.execute(sql)
con.commit()
# 5) 자원해제
con.close()
print('-'*30)

