import requests
import re

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)

locations = re.findall(r'<location wl_ver="3">(.+?)</location>', recvd.text, re.DOTALL)


for location in locations:
    
    province = re.findall(r'<province>(.+?)</province>', location, re.DOTALL)
    pc = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>', location, re.DOTALL)
    province = pc[0][0]
    city = pc[0][1]
    # print(province, city)
    datas = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)
    for data in datas:
        weather_regex= re.compile(r"""<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>.+?<tmn>(.+?)</tmn>.+?<tmx>(.+?)</tmx>.+?<reliability></reliability>.+?<rnSt>(.+?)</rnSt>.+?""", re.DOTALL)
        weather = weather_regex.findall(data)[0]
        mode = weather[0]
        tmEf = weather[1]
        wf = weather[2]
        tmn = weather[3]
        tmx = weather[4]
        rnSt = weather[5]
        str = '{},{},{},{},{},{},{},{}'
        print(str.format(province, city, mode, tmEf, wf, tmn, tmx, rnSt))
    


