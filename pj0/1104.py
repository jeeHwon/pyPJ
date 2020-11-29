#딕션어리 : key와 value로 구성
people = {"name":"둘리", "age":"1억살","addr":"쌍문동"}
print(people)
print(type(people))
print(people["age"])
people["성격"]="불같음" #추가
print(people)
people["성격"]="차가움" #변경
print(people)
del people["age"] #삭제
print(people)

print("\n"*10)

for i in people:
    print(i)

for i in people.items():
    print(i)

for i, v in people.items():
    print(i,v)
people.clear()
print(people)

print("\n"*10)

#set{}
a = {2,5,3,7,2} #중복이 제거됨
print(a)
print(type(a))

b = [1,5,4,8,32,2,5,1,1]
print(b)
print(type(b))
print(set(b))   #list를 set으로 바꿔서 중복 제거됨
a.add(999)
print(a)
a.update(["으","랏","차"])
print(a)
a.remove(999)
print(a)
print("\n"*10)

#정규표현식
# ?	: 0번 또는 1차례까지의 발생
# *	: 0번 이상의 발생
# +	: 1번 이상의 발생
#{최소값, 최대값}
#{3}
#{,3}
#{3,}
# | 선택
# [a-zA-Z0-9%^&*()]
# \s 공백

a='''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

import re   #정규식 사용
# re.findall(r'정규식',문자열)
r1=re.findall(r'[0-9]',a)
print(r1)
r1=re.findall(r'[0-9]+',a)
print(r1)
r1=re.findall(r'[A-Za-z]+',a)
print(r1)
# T로 시작하지 않는 이름 찾기
r1=re.findall(r'[A-SU-Z][a-z]+',a)
print(r1)