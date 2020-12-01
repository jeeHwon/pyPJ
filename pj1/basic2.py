import basic
# logger = basic.logger
# def hap(n):
#     logger.info('hap 함수 호출')
#     h = 0
#     for i in range(n+1):
#         h = h + i
#         if h > 1000:
#             logger.critical('합이 1000을 초과, '+str(i)+', '+str(h))
#     return h
# print(hap(10))
# print(hap(100))

# try-except -----------------------------
# names =['kim', 'lee', 'park']
# try:
#     i = 'choi'
#     # print(names.index(i))
#     x=[1,2]
#     y='test'
#     z=x+y
# except ValueError:
#     print('해당값이 리스트에 없음')
# except TypeError:
#     print('리스트와 문자열을 연결못함')
# except:
#     print('예외발생')
# else:
#     print('ok')
# finally:
#     print('무조건 실행')


# 제너레이터--------------------------------
# n= [1,2,3,4,5]
# rn = reversed(n)
# print(rn)

# # 이터러블 : 리스트, 문자열, 튜플, 딕셔너리처럼 요소를 차례차례 꺼낼수 있는 객체
# for c in 'python':
#     print(c)

# # 이터레이터: 이터러블 중에서 next() 함수를 사용해서 요소를 하나하나 꺼낼 수 있는  
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))

def test():
    print('test함수 호출')
    yield 'test'

print('a')
test()
print('b')
test()

print(test())

# 제너레이터 함수 : 제너레이터를 리턴하는 함수
# 제너레이터 next() 함수를 이용하여 함수의 내부코드 실행

def test1():
    print('one')
    yield 111
    print('two')
    yield 222
    print('three')
    
# r1 = test1()
# print('four')
# r2 = next(test1())
# print(r2)
# r2 = next(test1())
# print(r2)
for i in test1():
    print('{}**'.format(i))

# 아나콘다 설치, 가상환경 설정, 스크래피 설정, 쥬피터 노트북 사용법
# https://copycoding.tistory.com/60
# 가상환경 pj2 생성
