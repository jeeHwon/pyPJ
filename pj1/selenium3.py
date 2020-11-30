from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# url = 'http://pjt3591oo.github.io/'
# driver = webdriver.Chrome('data\\chromedriver.exe')
# driver.get(url) 
# driver.execute_script('alert("hi")')
# time.sleep(1)

# search = driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
# search.click()
# box = driver.find_element_by_css_selector('#search-box')
# box.send_keys('javascript')

# # 마우스 클릭 대신 엔터키로 이동하기
# box.send_keys(Keys.ENTER)


# h3s = driver.find_elements_by_css_selector('#search-results > li > a > h3')
# for h3 in h3s:
#     print(h3.text)

# 만개의 레시피에서 자바스크립트 링크된 태그 실행하기
# url = 'https://www.10000recipe.com/recipe/list.html'
# driver = webdriver.Chrome('data\\chromedriver.exe')
# driver.get(url) 

# a2 = driver.find_element_by_css_selector('#id_search_category > table > tbody > tr:nth-child(1) > td > div > div:nth-child(1) > a:nth-child(2)')
# print(a2.text)
# print(a2.get_attribute(('href')))
# driver.execute_script(a2.get_attribute(('href')))

# import urllib.request
# url = 'https://shared-comic.pstatic.net/thumb/webtoon/739115/thumbnail/thumbnail_IMAG04_6fd7bfbe-10da-44c7-9707-8c56552fe337.jpg'
# filename = 'img/web1.jpg'
# urllib.request.urlretrieve(url, filename)

from urllib.parse import urlparse
url = 'https://www.ml5.co.kr:1621/a502/index.html?student=14&area=60#title'
pr = urlparse(url) # 네임드 튜플 반환
print(urlparse(url))
print(pr.scheme)    #http, ftp,...
print(pr.netloc)    #네트워크 위치
print(pr.path)      #경로
print(pr.query)     #쿼리
print(pr.fragment)     #프래그먼트(위치)

# from urllib.parse import urljoin
# baseurl = 'https://www.ml5.co.kr:1621/a502/index.html?student=14&area=60'
# print("원래", baseurl)
# print(1, urljoin(baseurl, 'main.html'))
# print(2, urljoin(baseurl, '/main.html'))
# print(3, urljoin(baseurl, '/a501/index.html'))
# print(4, urljoin(baseurl, '../img/a.jpg'))
# print(5, urljoin(baseurl, '//img/a.jpg'))
# print(6, urljoin(baseurl, '//img/a.jpg'))

# import os
# name1 = 'd:\\study\\pj1\\data\\Beauty.smi' # window에서나 먹지
# name2 = os.path.join('d:\\', 'study', 'pj1', 'data', 'Beauty.smi') # 개발자라면 이렇게쓰자
# print('name1의 경로',name1)
# print('name1의 dirname', os.path.dirname(name1))
# print('name1의 basename', os.path.basename(name1))
# print('-'*30)
# print(name2)

import os
print(os.path.exists('d:\\study\\pj1\\data'))   # 존재하니까 True   
print(os.path.exists('d:\\study\\pj1\\data2'))  # 존재하지 않으니까 False

# if not os.path.exists('d:\\study\\pj1\\data2'):
#     os.mkdir('d:\\study\\pj1\\data2')
a = [i for i in range(5)]
print(a)
b = ['one', 'two', 'three']
print(b)
print(a+b)
a.append(b)
print(a)