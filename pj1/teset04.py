# 네이버 API 이용하여 '머신러닝' 책 검색하여
# 책 제목, 책 이미지 url, 저가, 가격, 출판사, 상세설명을 200건 데이터 베이스 저장
# DB: MariaDB
import os
import sys
import json
import urllib.request
import pymysql
client_id = "tTUnbnTf9yFMsBYKKP5Q" # 개발자센터에서 발급받은 Client ID 값
client_secret = "qTzppGiOMG" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("머신러닝")

url = "https://openapi.naver.com/v1/search/book.json?start={}&display=100&query="+encText
conn = pymysql.connect(host='localhost', port=3307, user='root', password='asdf1038', db='Investar', charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)

for s in range(1, 200, 100):
    url = url.format(s)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    result = ''
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
    dic = json.loads(result)

    #검색 결과의 items 목록의 각 항목(post)을 출력
    for post in dic['items']:
        title = post['title'].replace('<b>','').replace('</b>','').replace(')','').replace('(','').replace('《','').replace('》','').replace('!','').replace('"','').replace("'",'').replace("|",'').replace("/",'').replace(",",'').replace(".",'').replace("ㆍ",'').replace("-",'')
        imageUrl = post['image']
        if imageUrl.find('?'):
            imageUrl = imageUrl[:imageUrl.find('?')]
        author = post['author']
        price = post['price']
        publisher = post['publisher']
        description = post['description'].replace('<b>','').replace('</b>','').replace(')','').replace('(','').replace('《','').replace('》','').replace('!','').replace('"','').replace("'",'').replace("|",'').replace("/",'').replace(",",'').replace(".",'').replace("ㆍ",'')

        str = '{}\n{}\n{}\n{}\n{}\n{}\n'
        str = str.format(title, imageUrl, author, price, publisher, description)
        print(str)
        break
        #쿼리 생성
        sql = "insert into book (title, imageUrl, author, price, publisher, description) values(%s, %s, %s, %s, %s, %s)"

        # 실행처리
        try: 
            cur.execute(sql,(title, imageUrl, author, price, publisher, description))
            conn.commit()
        except:
            continue
conn.close()


# # 4-1) 데이터 출력
# conn = pymysql.connect(host='localhost', port=3307, user='root', password='asdf1038', db='Investar', charset='utf8')
# cur = conn.cursor(pymysql.cursors.DictCursor)
# sql = 'select * from book'
# cur.execute(sql)
# rows = cur.fetchall()
# for row in rows:
#     # print(row)
#     print(row['title'], row['imageUrl'],row['author'],row['price'],row['publisher'], row['description'])
# conn.commit()

# # 5) 자원해제
# conn.close()

# create table book(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title varchar(200),
#     imageUrl varchar(200),
#     author varchar(200),
#     price varchar(10),
#     publisher varchar(200),
#     description varchar(200)
# );