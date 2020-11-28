# 영화제목 점수 예매율, 상영시간을 추출하여 movie.csv로 저장
# 영화 포스터는 img 폴더에 저장

import requests
import re
from bs4 import BeautifulSoup
# def saveImg(imgUrl, title):
#     filename ='img\\'+title+imgUrl[-4:]
#     r = requests.get(imgUrl)
#     print(filename)
#     with open(filename, 'wb') as f1:  # wb : write binary(이진파일로 써라)
#         f1.write(r.content)

# with open('data\\movie.csv','w',encoding='utf-8') as f:
#     pageurl = 'https://movie.naver.com/movie/running/current.nhn'
#     recvd = requests.get(pageurl)
#     # print(recvd) # <Response [200]> : 받아오기 성공
#     dom = BeautifulSoup(recvd.text, 'lxml')
#     ul = dom.find('ul', class_='lst_detail_t1')
#     dt = ul.find_all('dt', class_='tit')
#     dt_img = ul.find_all('div', class_='thumb')
#     dd = ul.find_all('div', class_='star_t1')
#     dd_time = ul.find_all('dl', class_='info_txt1')

#     for i in range(0,len(dt)):
#         title = dt[i].find('a').text
#         imgUrl = dt_img[i].find('img')['src']
#         imgUrl = imgUrl[:imgUrl.rfind('?')]
#         saveImg(imgUrl, title)
#         star = dd[i].find('span', class_='num').text
#         try:
#             rate = dd[i].find('dl', class_='info_exp').find('span', class_='num').text+"%"
#         except:
#             rate = '0%'

#         rtime = dd_time[i].find('dd').text
#         pattern = re.compile(r'\s+')
#         rtime = re.sub(pattern, '', rtime)
#         rtime = rtime[rtime.find('|')+1:rtime.rfind('|')]
#         f.write('{},{},{},{}\n'.format(title, star, rate,rtime))

#         print(title)
#         print(imgUrl)
#         print(star)
#         print(rate)
#         print(rtime)

#teacher version
import os
def saveImg(imgUrl, title):
    print(imgUrl)
    filename = 'img\\'+'mvImg_'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
    r = requests.get(imgUrl)
    with open(filename, 'wb') as f1:
        f1.write(r.content)

with open(os.path.join('data','movies.csv'),'w', encoding='utf-8') as f:
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
        saveImg(img, title)
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
        
        str = '%s,%s,%s,%s\n'%(title, rating, reserv, playtime)
        f.write(str)