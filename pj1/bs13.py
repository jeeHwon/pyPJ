import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# 보배드림 사이트 스크레이핑

url = 'https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=I'
recvd = requests.get(url)
print(recvd)

# 상세페이지의 기본정보를 데이터베이스에 입력, 이미지 car 폴더에 저장
#listCont > div.wrap-thumb-list > ul > li:nth-child(1) > div > div.mode-cell.title > p > a

dom = BeautifulSoup(recvd.text, 'lxml')
alist = dom.select('#listCont div.mode-cell.title > p.tit > a')
# print(len(alist))

baseurl = 'https://bobaedream.co.kr/'
urllist = []
for a in alist:
    # print(a['href'])
    urllist.append(urljoin(baseurl, a['href']))
# print(urllist)
for detailurl in urllist:
    r = requests.get(detailurl)
    detaildom = BeautifulSoup(r.text, 'lxml')
    title = detaildom.select_one('#bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.title-area > h3').text
    price = detaildom.select_one('#bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.price-area > span > b').text
    # year = detaildom.select_one('#bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.title-area > p > span:nth-child(1)').text
    # distance = detaildom.select_one('#bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.title-area > p > span:nth-child(2)').text
    # fuel = detaildom.select_one('#bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.title-area > p > span:nth-child(3)').text
    # color = detaildom.select_one('#bobaeConent > div.component.page-detail > div.container-detail > div.detail-section.mode-half > div:nth-child(1) > div.info-basic > div > table > tbody > tr:nth-child(1) > td:nth-child(4)').text
    
    # print(title, year, distance, fuel, price, color)
    imgs = detaildom.select('#bx-pager img')
    imglist=[]
    for img in imgs:
        if img['src'][2:6] == 'file':
            imglist.append('https:'+img['src'])
        # print(imglist)
    infos = detaildom.select('#bobaeConent > div.component.page-detail > div.container-detail > div.detail-section.mode-half > div:nth-child(1) > div.info-basic > div > table tr')
    # print(infos[0].text)
    infolist =infos[0].text.strip().split('\n')
    # print(infolist)
    year = infolist[1]
    baegi = infolist[-1]
    infolist =infos[1].text.strip().split('\n')
    # print(infolist)
    distance = infolist[1]
    color = infolist[-1]
    infolist =infos[2].text.strip().split('\n')
    # print(infolist)
    trans = infolist[1]
    guarantee = infolist[-1]
    infolist =infos[3].text.strip().split('\n')
    # print(infolist)
    fuel = infolist[1]
    check = infolist[-1]
    str = "연식:{}, 배기량:{}, 거리:{}, 색상:{}, 변속기:{}, 보증:{}, 연료:{}, 확인:{}";
    str = str.format(year,baegi,distance,color,trans,guarantee,fuel,check)
    print(str)
    break