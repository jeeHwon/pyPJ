import requests
from bs4 import BeautifulSoup
import json
import datetime

# 특정 시간에 자동으로 데이터 받기
with open('D:\\study\\pj1\\data\\sports_re.csv', 'a', encoding='utf-8') as f:
    pageurl = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
    recvd = requests.get(pageurl)
    dic = json.loads(recvd.text)
    now = datetime.datetime.now()
    print(now)
    for i in dic['list']:
        str = '===={}====\n{}\n'.format(i['title'], i['subContent'] )
        f.write(str+'\n')
        
print("sucess!!!!")

# 파이썬을 exe 파일로 만들기
# cmd에서 pyinstaller sports.py -> 오류 많아
# cmd에서 pyinstaller --onefile sports.py