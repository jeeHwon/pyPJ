a = "  blue red green "
print(len(a))  # 길이
print("[" + a + "]")
print("[" + a.lstrip() + "]")  # 왼쪽공백 삭제
print("[" + a.rstrip() + "]")  # 오른쪽공백 삭제
print("[" + a.strip() + "]")  # 양쪽공백 삭제
# a.replace('찾는 문자열','바꿀 문자열') : 문자열 치환
print("[" + a.replace(' ', '') + "]")
print(a.upper(), a.lower())
print("\n\n\n\n\n\n\n\n\n\n\n\n")

a = "one-two-three four-five six"
print(type(a))
print(a.split("-"))
print(a.split(" "))
print(type(a.split(" ")))  # <class 'list'>
b = a.split(' ')
print(b)
print('@'.join(b))
print('%'.join(b))
print("\n\n\n\n\n\n\n\n\n\n\n\n")

# print('문자열을 입력하세요')
# line = input()
# print("입력한 내용은 : " + line)
# print(line.split())

# print("\n\n\n\n\n\n\n\n\n\n\n\n")
# line = input()
# print(line, type(line))
# print(line.split())

# collection :
# [] 리스트
# () 튜플
# {} 딕셔너리, set
# <> not used

a = [1, 56, '아이유', ['one','two','three', True, 3.14]]
print(a)
print(a[2])
print(a[3:])
print(a[3][2])
print("\n\n\n\n\n\n\n\n\n\n\n\n")

b = ['사과','포도','키위']
b[1] = '거봉'
b.append('멜론')  #추가
print(b)
print(sorted(b))    #정렬
print("\n\n\n\n\n\n\n\n\n\n\n\n")

c = [2,78,144,5]
print('합계:',sum(c))
print('평균:',sum(c)/len(c))
print(dir(c))   #c 라는 객체에 사용할 수 있는 함수





