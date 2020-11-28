# import bs4 여기에서 일부만 필요하니까 다 가져오지 말자
import requests
url = 'https://www.naver.com'
recvd = requests.get(url)
#print(recvd)   #접근결과코드 : 200(성공)
#print(recvd.text)   #html코드
#print(recvd.encoding)   #인코딩 방식
#print(recvd.headers)
#print(recvd.content)


from bs5 import BeautifulSoup
# 웹페이지에 접근하여 태그 인식
f = open('data\\test.html', encoding='utf-8').read()
# print(f)
# BeautifulSoup(웹페이지, 파싱방식)
# 파싱 : html.paser, html5lib, lxml(태그 계층 구조를 인식하는 것)
# dom = BeautifulSoup(f, 'html.parser')   #body태그 안닫힌 문서도 태그 인식해서 채워준다
dom = BeautifulSoup(f, 'lxml')  # html.parser에 xml 포함. 속도 빠름
# print(dom)

# dom.find('태그')  # 첫번째 태그추출
# = dom.태그
# dom.find_all('태그') # 모든 태그 추출
# div = dom.find('div') 얘랑
# div = dom.div         # 얘랑 동일
# print(div)  # 첫번째 div 태그만 가져옴
# div = dom.find_all('div')
# print(div)  #[div1, div2,...]
# --------------------------------------

firstDiv = dom.div
div2 = firstDiv.div
# print(div2)
ps = div2.find_all('p')

# dom.find('태그', class_='클래스명')   # class_ : 예약어 피하기 위해서
# dom.find('태그', {'class': '클래스명'})
# cl = dom.find('div', class_='ex_class')   #아래와 동일
# print(cl)
# cl = dom.find(class_='ex_class')
# print(cl)

# dom.find_all(class_='클래스명')
# exs = dom.find_all('class_='ex_class')
# print(exs)
# sisters = dom.find_all(class_='sister')
# print(sisters)

# id가 third인 태그
third = dom.find(id='third')
#print(type(third))

# id가 third인 모든 태그
thirds = dom.find_all(id="third")
print(thirds[0])
print(type(thirds))





# import, main()


