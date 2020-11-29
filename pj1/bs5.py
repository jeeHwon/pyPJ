import requests
from bs4 import BeautifulSoup
import time

def saveImg(imgUrl, title):
    filename ='img\\'+title+imgUrl[-4:]
    r = requests.get(imgUrl)
    print(filename)
    with open(filename, 'wb') as f1:  # wb : write binary(이진파일로 써라)
        f1.write(r.content)

with open('data\\webtoon.csv','w',encoding='utf-8') as f:
    for page in range(1, 7):
        # url = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat'
        pageurl = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat&page={}'.format(page)
        recvd = requests.get(pageurl)
        # print(recvd) # <Response [200]> : 받아오기 성공
        dom = BeautifulSoup(recvd.text, 'lxml')
        table = dom.find('table', class_='viewList')
        trs = table.find_all('tr')
        # print(len(trs)) # 총 12개. 앞의 2개는 제목, 다음회미리보기로 제거한다
        for i in range(2, len(trs)):
            # print(trs[i])
            img = trs[i].find('img')['src']
            title = trs[i].find('td', class_='title').find('a').text
            saveImg(img, title)
            # title = title.find('a').text
            div = trs[i].find('div', class_='rating_type')
            star = div.find('strong').text
            regdate = trs[i].find('td', class_='num').text
            # f.write('{},{},{},{}\n'.format(img, title, star, regdate))
        # time.sleep(1)

# 모든 페이지의 이미지를 다운로드 하고 제목, 평점, 등록일을 webtoon.csv 파일로 저장
# 단, 한페이지당 1초 sleep
def saveImg(imgUrl, title):
    filename ='img\\'+title+imgUrl[-4:]
    r = requests.get(imgUrl)
    print(filename)
    with open(filename, 'wb') as f1:  # wb : write binary(이진파일로 써라)
        f1.write(r.content)

with open('data\\webtoon.csv','w',encoding='utf-8') as f:
    for page in range(1, 100):
        # url = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat'
        pageurl = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat&page={}'.format(page)
        recvd = requests.get(pageurl)
        # print(recvd) # <Response [200]> : 받아오기 성공
        dom = BeautifulSoup(recvd.text, 'lxml')
        table = dom.find('table', class_='viewList')
        trs = table.find_all('tr')
        # print(len(trs)) # 총 12개. 앞의 2개는 제목, 다음회미리보기로 제거한다
        for i in range(2, len(trs)):
            # print(trs[i])
            img = trs[i].find('img')['src']
            title = trs[i].find('td', class_='title').find('a').text
            saveImg(img, title)
            # title = title.find('a').text
            div = trs[i].find('div', class_='rating_type')
            star = div.find('strong').text
            regdate = trs[i].find('td', class_='num').text
            f.write('{},{},{}\n'.format(title, star, regdate))
        if len(trs) != 12:
            break

        time.sleep(1)

