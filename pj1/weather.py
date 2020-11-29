import requests
from bs4 import BeautifulSoup

with open('data\weather.csv', 'w', encoding='utf-8') as f:
    
    url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
    recvd = requests.get(url)
    # print(recvd.text)

    dom = BeautifulSoup(recvd.text, 'lxml')
    locations = dom.find_all('location')
    # print(len(locations)) # 41
    for location in locations:
        province = location.find('province').text
        city = location.find('city').text
        # print(province, city)
        datas = location.find_all('data')
        for data in datas:
            mode = data.find('mode').text
            tmef = data.find('tmef').text
            wf = data.find('wf').text
            tmn = data.find('tmn').text
            tmx = data.find('tmx').text
            rnst = data.find('rnst').text
            str = "{},{},{},{},{},{},{},{}\n".format(province,city,mode,tmef,wf,tmn,tmx,rnst)
            f.write(str)

