import os
import sys
import json
import urllib.request
from konlpy.tag import Okt 


client_id = "아이디"
client_secret = "비밀번호"
encText = urllib.parse.quote("전쟁")
url = "https://openapi.naver.com/v1/search/movie.json?start={}&display=100&query=" + encText # json 결과
for page in range(1,1001,100):
    request = urllib.request.Request(url.format(page))
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        result = response_body.decode('utf-8') # json
    else:
        print("Error Code:" + rescode)
    dic = json.loads(result)
    # print(dic)
    with open('data/movie.csv','a',encoding='utf-8') as f:
        for d in dic['items']: # [{}, {}, {}..]
            desc = d['title']
            desc = desc.replace('<b>전쟁</b>', '전쟁')
            desc = desc.replace('...', ' ')
            print(desc)
            f.write(desc+'\n')

with open('data/movie.csv', encoding='utf-8') as f:
    text = f.read()
okt = Okt()
lines = text.split('\n')
# print(len(lines))
word_dic = {}
stopwords = ['스탑할','단어적자']
for line in lines:
    mal = okt.pos(line, norm=True, stem=True)
    for m in mal:
        if (m[1] == 'Noun' or m[1] == 'Adjective') and len(m[0]) > 1 and m[0] not in stopwords:
            if not (m[0] in word_dic):
                word_dic[m[0]] = 0
            word_dic[m[0]] += 1
print(word_dic)

import operator
sdict= sorted(word_dic.items(), key=operator.itemgetter(1)) 
print(sdict)

# WordCloud로 출력
from PIL import Image
import numpy as np
img = Image.open('이미지주소')
mask = np.array(img)
from wordcloud import WordCloud
import matplotlib.pyplot as plt
dic = dict(sorted(word_dic.items(),key=lambda x:x[1],reverse=True)[:100])
wc = WordCloud(font_path='malgun.ttf',mask=mask).generate_from_frequencies(dic)
plt.imshow(wc)
plt.axis('off')
plt.show()