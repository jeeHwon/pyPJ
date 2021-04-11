import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select(".lwidth tbody .strong td em")

# css selector로 접근가능
# tags = soup.select("#content > div.section.invest_trend > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(4) > em")

for tag in tags:
    print(tag.text)
