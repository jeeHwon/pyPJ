a = [1, 5, 3, 6, 8, 5]
print(a)
print(len(a))
print(a.count(5))
a.append('seven')
a.append(['킬빌', '올드보이'])
print(a)
a.insert(2, '*')  # a.insert(인덱스, 값)
print(a)
a.remove(5)  # 리스트의 값 중 처음나온 5를 삭제
print(a)
del a[:3]  # a 리스트의 0번째부터 2번째까지 삭제
print(a)
del a  # 객체 삭제
# print(a) NameError: name 'a' is not defined
print('\n\n\n\n\n\n\n\n\n\n\n')

# for문
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for 변수 in 반복가능객체:
#     내용
for i in a:  # i=1,2,3..
    print(i)

# range(시작(0부턴 생략가능), 종료(<),증감(1씩은 생략가능))
print(range(1, 10, 1))
print(list(range(1, 10, 1)))

# 형변환
b = '3'
print(type(b))
print(type((int(b))))

for i in range(6):  # i=0,1,2,3,4,5
    print(i, a[i])
print('\n\n\n\n\n\n\n\n\n\n\n')

for i in range(len(a)):
    print(a[i])

# 1-100 숫자 출력
for i in range(1, 101):
    print(i, end=' ')
print()
for i in range(3, 1000, 3):
    print(i, end=' ')
print('\n\n\n\n\n\n\n\n\n\n\n')

# a=[0,1,2,3..100]
for i in range(101):
    print(i)
# 컴프리핸션
a = [i for i in range(101)]
print(a)

# b = [7,7,7....7]
for i in range(100):
    print(7)
    
b = [7 for i in range(100)]
print(b)
print(len(b))

c = []
for i in range(100):
    c.append(7)
print(c)    

# c = [1,3,5,..99]
# d = ['good','good',..백개]
c = [i for i in range(1,100,2)]
d = ['good' for _ in range(101)] # i는 변수로서 의미 없기 떄문에 _가능
print(c)
print(d)

e = ['good'+str(i*2) for i in range(5)]
print(e)
