# konlpy
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
# JPype1‑1.2.0‑cp36‑cp36m‑win_amd64.whl python 버전에 맞추어 다운로드
# pip install JPype1‑1.2.0‑cp36‑cp36m‑win_amd64.whl
# pip install konlpy

str = '잠겨 죽어도 좋으니 너는 물처럼 내게 밀려오랗ㅎㅎ'

from konlpy.tag import Hannanum
h = Hannanum()
# print(h.pos(str))
# print(h.nouns(str)) # 명사 추출
# print('='*30)

from konlpy.tag import Okt  
o = Okt()
# print(o.pos(str))
# print(o.pos(str, norm=True)) # 문장정규화
# print(o.pos(str, norm=True, stem=True)) # 문장정규화 + 원형추출
# print(o.nouns(str)) # 명사 추출
# print('='*30)

# 네이버 뉴스 검색 API
import os
import sys
import json
import urllib.request

# with open ('C:\\myKey\\naver.txt') as f:
#     pw = f.readline()
# client_id = "tTUnbnTf9yFMsBYKKP5Q"
# client_secret = pw
# encText = urllib.parse.quote("아이유")
# url = "https://openapi.naver.com/v1/search/news.json?start={}&display=100&query=" + encText # json 결과
# for page in range(1,1001,100):
#     request = urllib.request.Request(url.format(page))
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request)
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         # print(response_body.decode('utf-8'))
#         result = response_body.decode('utf-8') # json
#     else:
#         print("Error Code:" + rescode)
#     dic = json.loads(result)
#     # print(dic)
#     with open('data/news.csv','a',encoding='utf-8') as f:
#         for d in dic['items']: # [{}, {}, {}..]
#             desc = d['description']
#             desc = desc.replace('<b>아이유</b>', '아이유')
#             desc = desc.replace('...', ' ')
#             print(desc)
#             f.write(desc+'\n')

# dict 정렬
# a = [3,1,2]
# print(sorted(a))
# print(sorted(a, reverse=True))
# b = {'one':100, 'two':200, 'three':300}
# for i in b: # key
#     print(i)
# for i in b.items(): # (key, value)
#     print(i)
# print(sorted(b)) # ['one', 'three', 'two']
# print(sorted(b.items())) # [('one', 100), ('three', 300), ('two', 200)]
# print(sorted(b.items(), key=lambda x: x[1]))
# print(sorted(b.items(),key=lambda x: x[1], reverse=True))

# with open('data/news.csv', encoding='utf-8') as f:
#     text = f.read()
# okt = Okt()
# lines = text.split('\n')
# # print(len(lines))
# word_dic = {}
# stopwords = ['오인혜','조병규']
# for line in lines:
#     mal = okt.pos(line, norm=True, stem=True) # [('앰버', 'Noun'), ('서다', 'Verb'),
#     for m in mal:
#         if (m[1] == 'Noun' or m[1] == 'Adjective') and len(m[0]) > 1 and m[0] not in stopwords:
#             if not (m[0] in word_dic):
#                 word_dic[m[0]] = 0
#             word_dic[m[0]] += 1
# print(word_dic)
# 정렬 1)라이브러리 이용
# import operator
# sdict= sorted(word_dic.items(), key=operator.itemgetter(1)) # index 1 즉, value 기준 정렬
# print(sdict)
# 정렬 2) 람다이용
# sdict= sorted(word_dic.items(), key=lambda x: x[1]) # index 1 즉, value 기준 정렬
# print(sdict)

# WordCloud로 출력
from PIL import Image
import numpy as np
# img = Image.open('img/one.png')
# mask = np.array(img)
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# dic = dict(sorted(word_dic.items(),key=lambda x:x[1],reverse=True)[:100])
# wc = WordCloud(font_path='malgun.ttf',mask=mask).generate_from_frequencies(dic)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()


# IT/과학 뉴스
from tqdm import tqdm
with open('data/news2.csv', encoding='cp949') as f:
    text = f.read()
print(text)
okt = Okt()
lines = text.split('\n')
# print(len(lines))
word_dic = {}
stopwords = []
for line in tqdm(lines):
    mal = okt.pos(line, norm=True, stem=True) # [('앰버', 'Noun'), ('서다', 'Verb'),
    for m in mal:
        if (m[1] == 'Noun' or m[1] == 'Adjective') and len(m[0]) > 1 and m[0] not in stopwords:
            if not (m[0] in word_dic):
                word_dic[m[0]] = 0
            word_dic[m[0]] += 1
            
from PIL import Image
import numpy as np

img = Image.open('img/apple.png')
mask = np.array(img)
# print(mask)
# mask 오류 해결하기
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 1:
            mask[i][j] = 255
# print(mask)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
dic = dict(sorted(word_dic.items(),key=lambda x:x[1],reverse=True)[:100])
wc = WordCloud(font_path='malgun.ttf', mask=mask).generate_from_frequencies(dic)
plt.imshow(wc)
plt.axis('off')
plt.show()

