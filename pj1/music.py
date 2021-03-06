# 한국음악저작권 협회에서 저작물 받아오기(post 방식)
import requests
from bs4 import BeautifulSoup
import math
import os
import cx_Oracle

# create table music(
#     no number primary key,
#     title varchar2(100),
#     singer varchar2(100),
#     lyricist varchar2(100),
#     composer varchar2(100)
# );
# create sequence music_seq;

os.putenv('NLS_LANG', '.UTF8')
conn = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = conn.cursor()
url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
data = {'S_PAGENUMBER': 1,
    'S_MB_CD': '10000992',
    'S_HNAB_GBN': 'I',
    'hanmb_nm': '아이유',
    'sort_field': 'SORT_PBCTN_DAY'}
recvd = requests.post(url, data=data)

# 모든페이지에 있는 저작물명, 가수명, 작사, 작곡을 오라클에 저장

dom = BeautifulSoup(recvd.text, 'lxml')
pages = dom.find('div', class_='status_area').find('p').text.split('(')[-1]
pagesSlicingIdx = pages.find('개')
pageEnd = math.ceil(int(pages[:pagesSlicingIdx])/10)

for page in range(1, pageEnd+1):
    data = {'S_PAGENUMBER': '{}'.format(page),
    'S_MB_CD': '10000992',
    'S_HNAB_GBN': 'I',
    'hanmb_nm': '아이유',
    'sort_field': 'SORT_PBCTN_DAY'}
    recvd = requests.post(url, data=data)
    dom = BeautifulSoup(recvd.text, 'lxml')
    tables = dom.find_all('table')
    trs = tables[1].find_all('tr')

    for i in range(1,len(trs)):
        title =  trs[i].find_all('td')[0].text
        singer = trs[i].find_all('td')[1].text
        lyricist = trs[i].find_all('td')[2].text
        composer = trs[i].find_all('td')[3].text
        sql = "insert into music values (music_seq.nextval, '{}', '{}', '{}', '{}')"
        try :
            cur.execute(sql.format(title, singer, lyricist, composer))
            print('{} DB 입력 완료'.format(title))
        except :
            print('error')
            continue
conn.commit()
conn.close()