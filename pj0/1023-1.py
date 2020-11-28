# 파이썬의 모든 것은 객체
# 변수 앞에 아무것도 없음
# 문자의 끝에 ; 없음
# 따움표'',""
# 문장의 세로줄을 맞추어야함
# 주석 #
# 도움말 ctrl + click

# a = 3
# print(a)
# a = "hello"
# print(a)
# a = True
# print("a의 값은=",a,"그럼 이만",sep='*', end='')
# print("새로운줄")
# print('-'*30)

# a=30
# b=5
# print(a,b)
# print(type(a)) #<class 'int'>
# a='machine'
# print(type(a)) #<class 'str'>

# 형변환
# print('a의 값은='+str(b))

# a = 5
# b = 10
# a, b = b, a
# print(a,b)
# a,b,c,d = 1,2.0,True,"문자"
# print(a,b,c,d)
# print(type(a),type(b),type(c),type(d))
# print(bool(0)) #0은 false 그외 true
# print(bool(33))

# 사칙연산자
a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫
print(a%b)  #나머지
print(a**b)
print('\n\n\n\n')

# 비교연산자
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print('\n\n')
# age=21
# b1=age<10
# b2=age>20
# print(b1,b2)
# print(10<=age<=30)
# print('\n\n')

# 문자열 : '..' ".." '''...''' """..."""
# a='문자열 표현방법!@#'
# print(a)
# a='문자열\' 표현방법!@#'
# print(a)
# a='''손흥민이 교체로 출전해 득점한 토트넘 홋스퍼가 유로파리그
# 첫 승을 신고했다.토트넘은 23일(한국시간) 영국 런던의 토트넘
# 홋스퍼 스타디움에서 열린 LASK린츠(오스트리아)와의 2020~2021
# 유럽축구연맹(UEFA) 유로파리그 조별리그 J조 1차전에서 3-0 승리했다'''
# print(a)

# 문자열 연산자이용
# a='python'
# b='machine'
# print(a+b)
# print(a*5)
print('\n\n\n\n')

# 문자열 인덱싱 : 문자열중에서 특정 데이터를 획득, []
# [인덱스]
# [시작인덱스:끝인덱스]  시작인덱스 <= x < 끝인덱스
a='0123456789'
print(a[3])
print(a[-2])
print(a[3:7])
print(a[3:-3])
print(a[:4])
print(a[4:])
print('\n\n\n\n')

# 문자열 수정해서 출력하기
a='pithon'
# a[1]='y' 문자열은 그 요소값을 변경 할 수는 없음
print(a[:1]+'y'+a[2:])
print('\n\n\n\n')

# 포맷팅
a=10
b=20
c='green'
print(a,b,c)
print('%s + %s = [%s%%]'%(a,b,c))
# print('%d + %d = [%d]'%(a,b,c))
# %s:문자열 %d:정수 %f:실수 %o8:8진수 %x:16진수 %%:%
print("{} + {} = {}".format(a,b,c)) #python 3.x 이후 가능
print('\n\n\n\n')

# count, find, index
a='1223334444'
print(a.count('0'))
print(a.count('3'))
print(a.find('0')) #없으면 -1
print(a.find('4')) #중복시엔 가장 앞위치
#print(a.index('0')) #find랑 같은데 없으면 에러
print(a.index('4'))





