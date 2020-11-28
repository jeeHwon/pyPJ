# movies.csv와 mariadb 연동

import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', port=3307, user='root', password='asdf1038', db='pythondb', charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor) 

sql = 'insert into movie (title, rating, reserv, playtime) values(%s, %s, %s, %s)'

pageurl = 'https://movie.naver.com/movie/running/current.nhn'
recvd = requests.get(pageurl)
dom = BeautifulSoup(recvd.text, 'lxml')
ul = dom.find('ul', class_='lst_detail_t1')
lis = ul.find_all('li')
for li in lis:
    img = li.find('img')['src']
    title = li.find('dt', class_='tit').find('a').text
    if title.count(':')==1:
        title = title.replace(':','')
    rating = li.find('span', class_='num').text
    reserv = li.find('div', class_='star_t1 b_star')
    if reserv == None:
        temp = '예매정보없음'
    else :
        temp = reserv.find('span', class_='num').text
    reserv = temp
    ptime = li.find('dl', class_='info_txt1').text
    ptimeList = ptime.split('|')
    playtime=''
    for p in ptimeList:
        if p.count('분') == 1:
            if p.count('개요') ==1:
                p=p.replace('개요','')
            playtime = p.strip()
            break
    cur.execute(sql,(title, rating, reserv, playtime))
conn.commit()
conn.close()