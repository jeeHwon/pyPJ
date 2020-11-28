# n = int(input('숫자(1-3)'))
# if n == 1:
#     print('hi')
# elif n == 2:
#     print('hi'*2)
# elif n == 3:
#     print('hi'*3)
# else:
#     print('hi'*4)

# n = int(input('숫자='))
# a = []
# for i in range(n):
#     a.append('Hi')
# print(a)

# n = int(input('숫자='))
# a = ['hi' for i in range(n)]
# print(a)

#1-20 홀수 중 3의 배수인것만 b에 넣기
# b = []
# for i in range(1, 21, 2):
#     if i % 3 == 0:
#         b.append(i)
# print(b)

#-> 컴프리핸션 : 컬렉션을ㅇ 만드는 한줄짜리 반복문
# b = [i for i in range(1, 21, 2) if i % 3 == 0]
# print(b)

#튜플 : 변경 불가 /사용법은 list와 같다 /파이썬이 매개변수 전달시 주로사용
# a = ('감', '사과', '대추')
# print(a, type(a))
# for i in a:
#     print(i)
# print(a, type(a))

#인덱스와 같이 출력
# a = ('빨', '주', '노')
# for i in enumerate(a):
#     print(i)
# print('-'*30)
# for i, v in enumerate(a):
#     print(i, v)

# a, b, c = 1, 'two', '셋'
# print(a, b, c)
# a = 1, 'two', '셋'
# print(a)
# 
# a = range(10)
# print(a)
# print(list(a))
# print(tuple(a))

#딕션어리{} : 순서x 키와 값 세트, 키는 중복x 값은 가능
# friend = {'name': 'kim', 'age': 20, 4885: 'yes'}
# print(friend, type(friend))
# print(friend['age'])
# print(friend[4885])
# print('-'*30)
# for i in friend:
#     print(i, friend[i])
# print('-'*30)
#
# print(friend.keys())    #키 반환
# print(friend.values())  #값 반환
# print('-'*30)
#
# for i in friend.items():    #키와 값 반환
#     print(i)
# for i, v in friend.items():
#     print(i, v)

a = 'javascript'
for i in a:
    print(a)
r = [i for i in a]
print(r)
for i in enumerate(a):
    print(i)
r = {}
for i in enumerate(a):
    r[i[0]]=i[1]
print(r)
r = {i[1]: i[0] for i in enumerate(a)}
print(r)
