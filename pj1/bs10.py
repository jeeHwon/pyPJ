import requests
from bs4 import BeautifulSoup

#https://imgnews.pstatic.net/image/001/
# 2020/11/26/PGT20200823121801055_P4_20201126092414621.jpg?type=w647
def saveImg(imgUrl, title):
    jpg = imgUrl[ imgUrl.index('?')-4 : imgUrl.index('?') ] # .jpg
    title = title.replace('[','')
    title = title.replace(']','')
    title = title.replace('"','')
    title = title.replace("'",'')
    title = title.replace('!','')
    title = title.replace('?','')
    title = title.replace(',','')
    title = title.replace('.','')
    filename = 'img\\'+ title + jpg
    # print(filename)
    r = requests.get(imgUrl)
    f =open(filename, 'wb')
    f.write(r.content)
    f.close()

def makeData(pageUrl):
    r = requests.get(pageUrl)
    d = BeautifulSoup(r.text, 'lxml')
    imgUrl = d.find('div', id='newsEndContents').find('img')['src']
    title = d.find('h4').text
    content = d.find('div', id='newsEndContents').text
    str = '==={}===\n{}'.format(title, content)
    saveImg(imgUrl,title)
    # print(str)
    # print(imgUrl)


url = 'https://sports.news.naver.com/index.nhn'
recvd = requests.get(url)

dom = BeautifulSoup(recvd.text, 'lxml')
aes = dom.find_all('a', class_='link_today')
# https://sports.news.naver.com/news.nhn?oid=109&aid=0004317073
for a in aes:
    pageUrl = 'https://sports.news.naver.com'+a['href']
    makeData(pageUrl)
    
