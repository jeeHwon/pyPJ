# 변수 = open('파일명',모드)
# 사용
# 변수.close() 자원반납
# 모드 : r(읽기), w(쓰기), a(추가)
f = open('data\\poem.txt', encoding='utf-8')
txt = f.read() #전체읽기
# txt = f.read(10) 10글자 읽기
print(type(txt))
print(txt)
f.close()
print('-'*30)

# 윈도우에서 슬래쉬 두개 주는 것을 원칙
f = open('data\\poem.txt', encoding='utf-8')
txt = f.readline()  #한줄 읽기
print(type(txt))    #문자열
print(txt)
f.close()
print('-'*30)

# mode 안쓰면 기본값으로 'r'로 설정되어 있음
f = open('data\\poem.txt', encoding='utf-8')
txt = f.readlines()  # 줄단위 리스트 반환
print(type(txt))    # 리스트
for line in txt:
    print(line.strip()) # strip() : 양 끝 공백 및 특수문자 제거
f.close()
print('-'*30)

# with open('파일명',모드) as 변수명 :
#   => with 블럭이 끝날 때 자동 close
with open('data\\poem.txt', encoding='utf-8') as f:
    txt = f.read()
    print(txt)
print('-'*30)

with open('data\\test1.txt', mode='w', encoding='utf-8') as f:
    f.write('very good day')
    f.write(' 한글은 안보이나요?')
print('-'*30)

# (mode=) 는 생략가능
with open('data\\test1.txt', 'a', encoding='utf-8') as f:
    f.write('잘 보이네여 하핫')
    for i in range(100):
        f.write(str(i**2)+'\n')
print('-' * 30)

dest = ['aa', 'bb', 'cc']
with open('data\\test1.txt', 'a', encoding='utf-8') as f:
    for a in dest:
        f.writelines(dest)
print('-' * 30)

with open('data\\test1.txt', 'w') as f:
    print('test print', file=f)
print('-' * 30)

col = ['이름', '나이', '주소']
names = ['jenny', 'rose', 'jisoo', 'risa']
age = [24, 23, 26, 25]
juso = ['서산', '남원', '동해', '벌교']
with open('data\\addr.txt', 'w', encoding='utf-8') as f:
    f.write(','.join(col)+'\n')
    for i in range(len(names)): #i = 0, 1, 2, 3
        str = '{},{},{}\n'.format(names[i], age[i], juso[i])
        f.write(str)
        print(str)
print('-' * 30)

# 연결문자.join(리스트)
a = ['010', '9793', '8419']
print('-'.join(a))
print('-' * 30)

# 이미지 저장
import requests #웹서버에 접근
url = 'https://movie-phinf.pstatic.net/20200622_64/15927889581932gf40_JPEG/movie_image.jpg'
recvd = requests.get(url)
print(recvd)    #<Response [200]> : HTTP 상태 코드로서 2xx는 성공
with open('img\\movie.jpg','wb') as f:  #wb : write binary(이진파일로 써라)
    f.write(recvd.content)








