# https://www.alexa.com/topsites 에서
# Rank, Site, Daily Time on Site, Daily Pageveiw per Visitor, % of Traffic From Search, Total Sites Linking In 수집 후 출력
import requests
from bs4 import BeautifulSoup

url = "https://www.alexa.com/topsites"
recvd = requests.get(url)
dom = BeautifulSoup(recvd.text, 'lxml')
table = dom.find('div', class_='listings table')
divs = table.find_all('div', class_='site-listing')

# 콘솔에 출력하기
# for i in range (len(divs)):
#     rank = divs[i].find('div', class_='td').text.strip()
#     site = divs[i].find('div', class_='DescriptionCell').text.strip()
#     dailyTime = divs[i].find_all('div', class_='right')[0].text.strip()
#     dailyView = divs[i].find_all('div', class_='right')[1].text.strip()
#     traffic = divs[i].find_all('div', class_='right')[2].text.strip()
#     linking = divs[i].find_all('div', class_='right')[3].text.strip()
#     print(rank, site, dailyTime, dailyView, traffic, linking)

# pandas로 출력
import pandas as pd
rankPd = []
sitePd = []
dailyTimePd = [] 
dailyViewPd = []
trafficPd = []
linkingPd = []
for i in range (len(divs)):
    rankPd.append(divs[i].find('div', class_='td').text.strip())
    sitePd.append(divs[i].find('div', class_='DescriptionCell').text.strip())
    dailyTimePd.append(divs[i].find_all('div', class_='right')[0].text.strip())
    dailyViewPd.append(divs[i].find_all('div', class_='right')[1].text.strip())
    trafficPd.append(divs[i].find_all('div', class_='right')[2].text.strip())
    linkingPd.append(divs[i].find_all('div', class_='right')[3].text.strip())
site_ = pd.Series(sitePd, index=rankPd, name='SITE')
dailyTime_ = pd.Series(dailyTimePd, index=rankPd, name='DAILY_TIME')
dailyView_ = pd.Series(dailyViewPd, index=rankPd, name='DAILY_VIEW')
traffic_ = pd.Series(trafficPd, index=rankPd, name='TRAFFIC')
linking_ = pd.Series(linkingPd, index=rankPd, name='LINKING')
df = pd.DataFrame({site_.name: site_, dailyTime_.name: dailyTime_, dailyView_.name:dailyView_, traffic_.name:traffic_, linking_.name:linking_})
print(df)