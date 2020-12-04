# https://www.alexa.com/topsites 에서
# Rank, Site, Daily Time on Site, Daily Pageveiw per Visitor, % of Traffic From Search, Total Sites Linking In 수집 후 출력

import requests
from bs4 import BeautifulSoup
import cx_Oracle
import os

os.putenv('NLS_LANG', '.UTF8')
conn = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = conn.cursor()
sql = "insert into ranking values (:1, :2, :3, :4, :5, :6)"

url = "https://www.alexa.com/topsites"
recvd = requests.get(url)
dom = BeautifulSoup(recvd.text, 'lxml')
table = dom.find('div', class_='listings table')
divs = table.find_all('div', class_='site-listing')

for i in range (len(divs)):
    rank = divs[i].find('div', class_='td').text.strip()
    site = divs[i].find('div', class_='DescriptionCell').text.strip()
    dailyTime = divs[i].find_all('div', class_='right')[0].text.strip()
    dailyView = divs[i].find_all('div', class_='right')[1].text.strip()
    traffic = divs[i].find_all('div', class_='right')[2].text.strip()
    linking = divs[i].find_all('div', class_='right')[3].text.strip()
    cur.execute(sql,(rank, site, dailyTime, dailyView, traffic, linking))
    # print(rank, site, dailyTime, dailyView, traffic, linking)

conn.commit()
conn.close()