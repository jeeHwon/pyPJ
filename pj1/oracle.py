# movies.csv와 oracle 연동

import requests
from bs4 import BeautifulSoup
import cx_Oracle
import os
os.putenv('NLS_LANG', '.UTF8')

conn = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = conn.cursor()
# sql = 'create sequence weboon_seq'
# cur.execute(sql)
# conn.commit()

sql = "insert into webtoon values (webtoon_seq.nextval, :1, :2, :3)"

for page in range(1, 100):
    pageurl = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat&page={}'.format(page)
    recvd = requests.get(pageurl)
    dom = BeautifulSoup(recvd.text, 'lxml')
    table = dom.find('table', class_='viewList')
    trs = table.find_all('tr')
    startidx = 2
    for i in range(startidx, len(trs)):
        img = trs[i].find('img')['src']
        title = trs[i].find('td', class_='title').find('a').text
        div = trs[i].find('div', class_='rating_type')
        star = div.find('strong').text
        regdate = trs[i].find('td', class_='num').text
        cur.execute(sql,(title, star, regdate))
    if len(trs) != 12:
        break
conn.commit()
conn.close()


# sql문 살짝 바꾼 version
import requests
from bs4 import BeautifulSoup
import cx_Oracle
import os
os.putenv('NLS_LANG', '.UTF8')

conn = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = conn.cursor()
# sql = 'create sequence weboon_seq'
# cur.execute(sql)
# conn.commit()



for page in range(1, 100):
    pageurl = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat&page={}'.format(page)
    recvd = requests.get(pageurl)
    dom = BeautifulSoup(recvd.text, 'lxml')
    table = dom.find('table', class_='viewList')
    trs = table.find_all('tr')
    startidx = 2
    for i in range(startidx, len(trs)):
        img = trs[i].find('img')['src']
        title = trs[i].find('td', class_='title').find('a').text
        div = trs[i].find('div', class_='rating_type')
        star = div.find('strong').text
        regdate = trs[i].find('td', class_='num').text
        sql = "insert into webtoon values (webtoon_seq.nextval, '{}', '{}', '{}')"
        cur.execute(sql.format(title, star, regdate))
    if len(trs) != 12:
        break
conn.commit()
conn.close()