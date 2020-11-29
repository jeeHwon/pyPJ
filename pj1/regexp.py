import re   #정규표현식(Regular Expression)

str = """
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
"""

# re.findall(r'패턴', 문자열)
# [x-z]  range를 표현하며 x ~ z 사이의 문자를 의미한다. 
# x+     반복을 표현하며 x 문자가 한번 이상 반복됨을 의미한다.
# x*     반복여부를 표현하며 x 문자가 0번 또는 그 이상 반복됨을 의미한다.
# x?     존재여부를 표현하며 x 문자가 존재할 수도, 존재하지 않을 수도 있음을 의미한다.
# .x     임의의 한 문자의 자리수를 표현하며 문자열이 x 로 끝난다는 것을 의미한
# x|y    or 를 표현하며 x 또는 y 문자가 존재함을 의미한다.
# x{n,m} 반복을 표현하며 x 문자가 최소 n번 이상 최대 m 번 이하로 반복됨을 의미한다.

r1 = re.findall(r'[0-9]', str) # []문자열 속에 하나
print(r1)
r2 = re.findall(r'[0-9]+', str) # []+하나이상
print(r2)
r3 = re.findall(r'[A-Z]+', str)
print(r3)
r4 = re.findall(r'[A-Za-z]+', str)
print(r4)

# . 줄바꿈을 제외한 한글자
print('='*40)
print(re.match('a.b', 'aabrrr'))
print(re.match('a.b', 'a0brrr'))
print(re.match('a.b', 'c0brrr'))
print(re.findall('a.b', 'aabrrr'))
print(re.search('a.b', 'aabrrr'))

print('='*40)
str = '3pink dress'
print(re.match('[a-z]+', str)) # 문자열 처음부터 정규식과 일치여부
print(re.search('[a-z]+', str))  # 문자열 전체를 검색하여 일치여부
print(re.findall('[a-z]+', str)) # 정규식에 일치하는 문자열 반환

# .group() 정규식에 일치하는 문자열 추출
print('='*40)
str = 'pink333 dress444'
print(re.match('[a-z]+', str).group()) 
print(re.search('[a-z]+', str).group())  
print(re.findall('[a-z]+', str)) 

print('='*40)
str = 'My handphone number 010-2222-3344이고 옛날폰은 011-3384-1564'
print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d', str))
print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d', str).group())
print(re.findall('\d\d\d-\d\d\d\d-\d\d\d\d', str))
print(re.findall('[0-9]{3,4}-[0-9]{3,4}-[0-9]{3,4}', str))
# print(re.match('\d\d\d-\d\d\d\d-\d\d\d\d', str).group())

print('='*40)
str = """
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
"""
# 옵션
# re.IGNORECASE(I) : 대소문자 구분X
# re.DOTALL(S) : 줄바꿈 포함
# re.VERBOSE(X) : 정규식에 주석을 사용할 수 있다
print(re.findall('[a-z]+', str, re.I))
t1 = re.compile('[a-z]+', re.I) # 정규식만 따로 저장가능
print(t1.findall(str))
print('\n'*40)

# 클립보드 이용해서 파이썬 외부에서 자료 가져올 때 사용
import pyperclip
# pyperclip.copy('hello python') # 복사 되는 메서드
# print(pyperclip.paste())    # 복사된 텍스트 콘솔출력 메서드


email_regex= re.compile(r"""(
    [a-zA-Z0-9_.-]+ # username
    @               # @ 기호
    [a-zA-Z0-9_.-]+  # 도메인
    (\.[a-zA-Z]+){1,2}  # com / co.kr...
    )""", re.VERBOSE)
text = pyperclip.paste()
result = email_regex.findall(text)
for r in result:
    print(r[0])

print('\n'*40)
f = open('data\\test.html', encoding='utf-8')
text = f.read()
# print(text)
tag = re.compile('<.*>')
print(tag.findall(text))
tag = re.compile('<.+>')
print(tag.findall(text))
tag = re.compile('<.+?>')
print(tag.findall(text))

# i로 시작하고 n으로 끝나는 모든 문자(greedy 방식) : 조건을 만족하는 가장 긴 문자열
str = 'internationalization'
text = re.compile(r'i.+n')
print(text.findall(str))

# i로 시작하고 n으로 끝나는 모든 문자(lazy 방식) : 조건을 만족하는 가장 짧은 문자열
str = 'internationalization'
text = re.compile(r'i.+?n')
print(text.findall(str))

reg = re.compile(r'i\>n')
print(reg.findall(text))