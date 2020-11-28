import requests
from bs4 import BeautifulSoup
import json

# 네이버 스포츠 뉴스 찾기
# # pageurl = 'https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N'
# # 위 page에는 찾고자 하는 정보 없어 네트워크로 찾아보면 아래 링크로 json 형태로 구성됨
# with open('data\sports.csv', 'w', encoding='utf-8') as f:
#     pageurl = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
#     recvd = requests.get(pageurl)
#     # BeautifulSoup로 받지 않고 json으로 바로 받는다
#     # dom = BeautifulSoup(recvd.text, 'lxml')
#     # print(recvd.text)
#     dic = json.loads(recvd.text)

#     for i in dic['list']:
#         str = '===={}====\n{}\n'.format(i['title'], i['subContent'] )
#         f.write(str)

# # 다음 증권에서 인기순위 가져오기
# from fake_useragent import UserAgent
# # with open('data\money.csv', 'w', encoding='utf-8') as f:
# with open('data\money.csv', 'w') as f:  # 한셀, 엑셀에서는 인코딩 안해야 글씨 안깨짐
#     ua = UserAgent()    # UserAgent ua = new UserAgent()
#     # print(ua.chrome)
#     headers = {'user-agent':ua.chrome,
#             'referer':'https://finance.daum.net/'}
#     pageurl = 'https://finance.daum.net/api/search/ranks?limit=10'
#     recvd = requests.get(pageurl, headers=headers)
#     dic = json.loads(recvd.text)
#     for i in dic['data'] :
#         str = '{}, {}, {}\n'.format(i['name'],i['tradePrice'],i['changeRate'])
#         f.write(str)


# import os
# import sys
# import json
# import urllib.request
# client_id = "tTUnbnTf9yFMsBYKKP5Q"
# client_secret = "qTzppGiOMG"
# encText = urllib.parse.quote("아이유")
# # url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog?display=100&query=" dispay 100개
# url = "https://openapi.naver.com/v1/search/blog?display=100&start=101&query=" + encText # 101부터시작

# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# result = ''
# if(rescode==200):
#     response_body = response.read()
#     result = response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
# dic = json.loads(result)
# print(dic)