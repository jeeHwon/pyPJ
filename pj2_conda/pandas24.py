import pandas as pd 
import urllib.request
import json

client_id = "tTUnbnTf9yFMsBYKKP5Q"
client_secret = "qTzppGiOMG"
encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/book.json?display=100&query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

result = ''
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
dic=json.loads(result)
# print(dic)
books = dic['items']
# print(books[0].keys())

# 책제목 출판사 가격 isbn 열을 데이터프레임 df로 생성
df = pd.DataFrame(books, columns=['title', 'publisher', 'price', 'isbn'])
df['price'] = df['price'].astype(float)
print(df)

# 출판사별 가격의 평균을 출력
print(df.groupby('publisher')['price'].mean())