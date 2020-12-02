import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time, os, datetime
import cx_Oracle
# 보배드림 사이트 스크레이핑 및 DB 연결

# DB 테이블 생성
# create table car(
#     no number constraint car_no_p primary key,
#     title varchar2(200),
#     price varchar2(200),
#     year varchar2(200),
#     baegi varchar2(200),
#     distance varchar2(200),
#     color varchar2(200),
#     trans varchar2(200),
#     guarantee varchar2(200),
#     fuel varchar2(200),
#     confirm varchar2(200)
# );
# create sequence car_seq;


# 이미지 저장함수
def saveImg(imglist, title):
    # try:
    i = 0
    for imgurl in imglist:
        i = i + 1
        filename = os.path.join('D:\\','study','pj1','car' ,title+str(i)+imgurl[-4:])
        print(filename)
        r1 = requests.get(imgurl)
        with open(filename, 'wb') as f:
            f.write(r1.content)
        print('저장완료:',filename)
    time.sleep(1)
    # except Exception as ex:
    #     print('img저장 에러발생 -> ',ex)

# DB 접속 및 쿼리문 생성
conn = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = conn.cursor()
sql = "insert into car values (car_seq.nextval, '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') "

# 페이지별 스크레이핑
url = 'https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=I&page={}&order=S11&view_size=20'
for page in range(1,4):
    recvd = requests.get(url.format(page))
    dom = BeautifulSoup(recvd.text, 'lxml')
    alist = dom.select('#listCont div.mode-cell.title > p.tit > a')

    baseurl = 'https://bobaedream.co.kr/'
    urllist = []
    for a in alist:
        urllist.append(urljoin(baseurl, a['href']))

    
    for detailurl in urllist:
        r = requests.get(detailurl)
        detaildom = BeautifulSoup(r.text, 'lxml')
        # 기본정보
        try:
            title = detaildom.select_one('#bobaeConent div.title-area > h3').text
            title = title.replace('\n','').replace(' ','').strip()
            price = detaildom.select_one('#bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.price-area > span > b').text
        except:
            continue

        # 이미지
        imgs = detaildom.select('#bx-pager img')
        imglist=[]
        for img in imgs:
            if img['src'][2:6] == 'file':
                imglist.append('https:'+img['src'])
        
        saveImg(imglist, title)
        

        # 상세정보
        infos = detaildom.select('#bobaeConent > div.component.page-detail > div.container-detail > div.detail-section.mode-half > div:nth-child(1) > div.info-basic > div > table tr')
        infolist =infos[0].text.strip().split('\n')
        year = infolist[1]
        baegi = infolist[-1]
        infolist =infos[1].text.strip().split('\n')
        distance = infolist[1]
        color = infolist[-1]
        infolist =infos[2].text.strip().split('\n')
        trans = infolist[1]
        guarantee = infolist[-1]
        infolist =infos[3].text.strip().split('\n')
        fuel = infolist[1]
        confirm = infolist[-1]
        strPrint = "연식:{}, 배기량:{}, 거리:{}, 색상:{}, 변속기:{}, 보증:{}, 연료:{}, 확인:{}"
        strPrint = strPrint.format(year,baegi,distance,color,trans,guarantee,fuel,confirm)
        # print("==============차량명: {}, 가격:{}==============".format(title, price))
        # print(str)
        
        # sql = sql.format(title,price,year,baegi,distance,color,trans,guarantee,fuel,confirm)
        # cur.execute(sql)
    time.sleep(1)
# conn.commit()
# conn.close()