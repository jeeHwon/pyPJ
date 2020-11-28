# 부처님 말씀 1000건 검색하여 제목과 상세내용을 blog.csv로 저장
# import os
# import sys
# import json
# import urllib.request
# client_id = "tTUnbnTf9yFMsBYKKP5Q"
# client_secret = "qTzppGiOMG"
# encText = urllib.parse.quote("유인나")
# with open('data\\blog.csv', 'w', encoding='utf-8') as f:

#     for i in range(1, 1000, 100) :
        
#         url = "https://openapi.naver.com/v1/search/blog?display=100&start={}&query=".format(i)+encText
#         request = urllib.request.Request(url)
#         request.add_header("X-Naver-Client-Id",client_id)
#         request.add_header("X-Naver-Client-Secret",client_secret)
#         response = urllib.request.urlopen(request)
#         rescode = response.getcode()
#         result = ''
#         if(rescode==200):
#             response_body = response.read()
#             result = response_body.decode('utf-8')
#         else:
#             print("Error Code:" + rescode)
#         dic = json.loads(result)
#         strFin = ''
#         for i in dic['items'] :
#             title = i['title']
#             title = title.replace('<b>','').replace('</b>','').replace('&lt;','').replace('&gt;','').replace('&quot;','')
#             content = i['description']
#             content = content.replace('<b>','').replace('</b>','').replace('&lt;','').replace('&gt;','').replace('&quot;','')
#             strFin = '{},{}\n'.format(title, content)
#             f.write(strFin)

# 네이버 영화 검색 API 이용
# import os
# import sys
# import json
# import urllib.request
# client_id = "tTUnbnTf9yFMsBYKKP5Q"
# client_secret = "qTzppGiOMG"
# encText = urllib.parse.quote("여름")

# url = "https://openapi.naver.com/v1/search/movie.json?start=1&display=100&query="+encText
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


# 파파고 번역
# import os
# import sys
# import urllib.request
# client_id = "aZA1DkMFMRKuN9guyVTi" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "BGskE9grTq" # 개발자센터에서 발급받은 Client Secret 값
# encText = urllib.parse.quote("오늘은 불금이네요, 하지만 사회적 거리두기 잖아요?")
# data = "source=ko&target=en&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

# i have a dream을 검색하여 한국어로 번역하세요
import os
import sys
import urllib.request
txt =''
with open('data\\transBefore.txt', encoding='utf-8') as f:
    txt = f.read()
    txt = txt.replace('\n', '')
    

print(txt)    
client_id = "aZA1DkMFMRKuN9guyVTi" # 개발자센터에서 발급받은 Client ID 값
client_secret = "BGskE9grTq" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote(txt)
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)