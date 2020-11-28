import os
import sys
import urllib.request
import json
client_id = "aZA1DkMFMRKuN9guyVTi"
client_secret = "BGskE9grTq"
encText = urllib.parse.quote("예림이 그 패 봐봐 장이야?")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
dic = json.loads(result)
print(dic['message']['result']['translatedText'])