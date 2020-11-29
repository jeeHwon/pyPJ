# 네이버 금융 시장지표에서 달러환율 가져오기
import requests
from bs4 import BeautifulSoup
# url = 'https://finance.naver.com/marketindex/'
# recvd = requests.get(url) # <Response [200]> : 받아오기 성공
# # print(recvd)
# # print(recvd.text)
# dom = BeautifulSoup(recvd.text, 'lxml')
# span = dom.find('span', class_='value')
# print(span.text)

# 네이버 웹툰에서 제목과 별점 가져오기
# url = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat'
# recvd = requests.get(url)
# # print(recvd) # <Response [200]> : 받아오기 성공
# dom = BeautifulSoup(recvd.text, 'lxml')
# table = dom.find('table', class_='viewList')
# trs = table.find_all('tr')
# # print(len(trs)) # 총 12개. 앞의 2개는 제목, 다음회미리보기로 제거한다
# for i in range(2, len(trs)):
#     # print(trs[i])
#     title = trs[i].find('td', class_='title')
#     a = title.find('a').text
#     div = trs[i].find('div', class_='rating_type')
#     star = div.find('strong').text
#     regdate = trs[i].find('td', class_='num').text
#     print('{},{},{}'.format(a, star, regdate))

# 네이버 웹툰에서 가져온 자료 파일로 쓰기
# with open('data\\webtoon.csv','w',encoding='utf-8') as f:
#     for page in range(1, 40):
#         # url = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat'
#         pageurl = 'https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat&page={}'.format(page)
#         recvd = requests.get(pageurl)
#         # print(recvd) # <Response [200]> : 받아오기 성공
#         dom = BeautifulSoup(recvd.text, 'lxml')
#         table = dom.find('table', class_='viewList')
#         trs = table.find_all('tr')
#         # print(len(trs)) # 총 12개. 앞의 2개는 제목, 다음회미리보기로 제거한다
#         for i in range(2, len(trs)):
#             # print(trs[i])
#             title = trs[i].find('td', class_='title')
#             a = title.find('a').text
#             div = trs[i].find('div', class_='rating_type')
#             star = div.find('strong').text
#             regdate = trs[i].find('td', class_='num').text
#             f.write('{},{},{}\n'.format(a, star, regdate))

# 이미지 경로까지 추가
import time
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
            title = trs[i].find('td', class_='title')
            a = title.find('a').text
            div = trs[i].find('div', class_='rating_type')
            star = div.find('strong').text
            regdate = trs[i].find('td', class_='num').text
            f.write('{},{},{},{}\n'.format(img, a, star, regdate))
        time.sleep(1)


# pageurl = 'https://pedia.watcha.com/ko-KR/users/R6OvKBeAjqN8V/contents/movies/ratings'
# recvd = requests.get(pageurl)
#
# dom = BeautifulSoup(recvd.text, 'lxml')
# ul = dom.find_all('ul', class_='css-w29x4j-VisualUl-ContentGrid-ContentGridUsedInArchive e14whxmg1')
# print(ul)

