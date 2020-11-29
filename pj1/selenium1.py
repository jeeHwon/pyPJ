from selenium import webdriver
import time
# 웹드라이버 : 크롤러와 브라우저를 연결시켜주는 프로그램
# 크롬 드라이버 다운로드 -> data 폴더에 exe 파일 넣기

url = 'http://pjt3591oo.github.io/'
driver = webdriver.Chrome('data\\chromedriver.exe')
driver.get(url) # 해당 페이지 접속
# print("현재 페이지소스:", driver.page_source)
# print("현재 url:",driver.current_url)
# print("title 태그:",driver.title)
# time.sleep(1)

# driver 이용방법
# 마우스제어 click()
# 키보드제어 send_keys()
# 자바스크립트 실행 execute_script()
# driver.find_element_by_class_name()
# driver.find_elements_by_class_name()
# driver.find_element_by_css_selector()
# driver.find_elements_by_css_selector()

# body > main > div > div > div:nth-child(9) > h3 > a
# a = driver.find_element_by_css_selector('body > main > div > div > div:nth-child(9) > h3 > a')
# print(a.tag_name)
# print(a.text)
# # a.click()

# body > header > div > nav > div > a:nth-child(4)
search = driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
search.click()
box = driver.find_element_by_css_selector('#search-box')
box.send_keys('python')
btn = driver.find_element_by_css_selector('body > main > div > div > form > input[type=submit]:nth-child(3)')
btn.click()

# 이건 별로다
# for i in range(1, 8):
#     title = driver.find_element_by_css_selector('#search-results > li:nth-child({}) > a > h3'.format(i)).text
#     print(title)
#search-results > li:nth-child(1) > a > h3
#search-results > li:nth-child(2) > a > h3

# elements로 다 받는게 더 좋지
h3s = driver.find_elements_by_css_selector('#search-results > li > a > h3')
for h3 in h3s:
    print(h3.text)