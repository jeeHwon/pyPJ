from selenium import webdriver
import time
import datetime

def getPwd():
    with open ('d:\\pw.txt') as f:
        pw = f.readline()
    return pw.strip()

url = 'https://pedia.watcha.com/ko-KR'
driver = webdriver.Chrome('data\\chromedriver.exe')
driver.get(url)
time.sleep(1)

loginStart = driver.find_element_by_css_selector('#root > div > div.css-1sh3zvx-NavContainer.ebsyszu0 > header > nav > div > div > ul > li:nth-child(6) > button')
loginStart.click()
time.sleep(1)

idbox = driver.find_element_by_css_selector('#sign_in_email')
idbox.send_keys('jswon9191@gmail.com')
time.sleep(1)

pwdbox = driver.find_element_by_css_selector('#sign_in_password')
pwdbox.send_keys(getPwd())
time.sleep(1)

loginBtn = driver.find_element_by_css_selector('#root > div > div.css-2k1shi-BackScreen.e5hxy7o0 > div > div > div > section > div > div > form > button')
loginBtn.click()
time.sleep(1)

url = 'https://pedia.watcha.com/ko-KR/users/R6OvKBeAjqN8V/contents/movies/ratings'
driver = webdriver.Chrome('data\\chromedriver.exe')
driver.get(url)
time.sleep(1)

# 스크롤 먼저 끝까지 내리기
SCROLL_PAUSE_SEC = 1

last_height = driver.execute_script("return document.body.scrollHeight")
print("last_height:",last_height)

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    print("new_height:",new_height)
    if new_height == last_height:
        break
    last_height = new_height


movies = driver.find_elements_by_css_selector('#root > div > div.css-1sh3zvx-NavContainer.ebsyszu0 > section > section > div.css-12hxjcc-StyledHideableBlock.e1pww8ij0 > section > div.css-1gkas1x-Grid.ejny11m0 > div > ul > li')

for movie in movies:
    title = movie.find_element_by_class_name("css-1y0pi15-ContentTitle").text
    star = movie.find_element_by_class_name("css-oab3z8-ContentRating").text.replace("평가함 ",'').replace('★ ','').strip()
    print(title, star)
