from selenium import webdriver
import time

def getPwd():
    with open ('d:\\pw.txt') as f:
        pw = f.readline()
    return pw.strip()

url = 'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
driver = webdriver.PhantomJS('data\\phantomjs.exe')
driver.get(url)
time.sleep(1)

idbox = driver.find_element_by_css_selector('#id')
idbox.send_keys('jswon91')
time.sleep(1)

pwdbox = driver.find_element_by_css_selector('#inputPwd')
pwdbox.send_keys(getPwd())
time.sleep(1)

loginBtn = driver.find_element_by_css_selector('#loginBtn')
loginBtn.click()
time.sleep(1)

driver.get('https://mail.daum.net/')
time.sleep(1)
print(driver.page_source)

# 보낸사람 제목출력
#mailList > div.scroll > div > ul > li:nth-child(1) > div.info_from > a
writers = driver.find_elements_by_css_selector('#mailList > div.scroll > div > ul > li > div.info_from > a')
for writer in writers:
    print(writer.text)

#mailList > div.scroll > div > ul > li:nth-child(2) > div.info_subject > a.link_subject > strong
titles = driver.find_elements_by_css_selector('#mailList > div.scroll > div > ul > li > div.info_subject > a.link_subject > strong')
for title in titles:
    print(title.text)