# 1) 함수정의
# def 함수명(매개변수):
#     내용
# 2) 함수호출
# 함수명(매개변수)

#f1('kim') 함수는 정의 후 사용
def f1(name) :
    print('hi~'+name)
#f1('kim')
#print(f1('lee')) #none 리턴값이 없으니까\

def f2(name) :
    return 'hi~'+name
#print(f2('lee'))

def f3(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1,y2,y3
#a,b,c=10,20,30
# r1,r2,r3 = f3(7)
# print(r1,r2,r3) #각각에 리턴

# r1 = f3(7)  #튜플로 리턴
# print(r1)

# print(list(r1)) 

def f4(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1,y2,y3]   #리스트로 리턴
# r1 = f4(8)
# print(r1)
# r1,r2,r3 = f4(8)
# print(r1,r2,r3)

def f5(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'y1':y1,'y2':y2,'y3':y3}  #딕션어리로 리턴
r1 = f5(3)
# print(r1)
# print(r1.keys(),r1.values())
# print(r1.items())

def f6(x,y) :
    print('f6 실행중')
    print(x,y)
#f6(3,4)
# f6(3,4,5) error

def f7(x=1,y=2,z=3) :
    print(x,y,z)
# f7()
# f7(11)
# f7(11,22)
# f7(11,22,33)
# f7(11,22,33,44) error

# def f8(x=1,y=2,z) : error
def f8(x,y,z=3) :
    print(x,y,z)

# f8()  error
# f8(10)    error
# f8(10,20)

#가변인수 : *, **
def f9(*args) :
    print(args)
    print(type(args))
    hap = 0
    for i in args :
        hap = hap + i
    print('hap=',hap)

# f9()
# f9(1,2,3)
# f9(1,2,3,4,5)
# f9('one','two') #error 숫자와 문자의 +오류

def f10(**args) :   #딕션어리로 매개변수 받을경우
    print(args)
    print(type(args))

#f10('a','b','c')
f10(name='kim',addr='busan',age=10)