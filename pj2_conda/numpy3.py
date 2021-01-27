import numpy as np 

# 데이터 생성
# a1 = np.array([[1,2,3],[4,5.,6]])
# print(a1)
# a2 = np.ones((2,4,2))
# print(a2)

# np.linspace(start,stop,개수,[속성])
# a3 = np.linspace(0,1,5) # start <= data <= stop
# print(a3)
# a3 = np.linspace(0,1,5,endpoint=False) # start <= data < stop
# print(a3)

# np.arage(시작, 종료, 증감)
# a3 = np.arange(10,20,2)
# print(a3)
# a3 = a3.astype(np.float)
# print(a3)
# a3 = a3.astype(np.int)
# print(a3)
# a3 = a3.astype(np.bool)
# print(a3)
# a3 = np.arange(10)  # 0부터 시작하고 증값값이 1인경우 종료값만 지정
# print(a3)
# a3 = np.arange(10,3,-1)
# print(a3)


# 난수 생성
# 변수 = np.random.randint(low, high, 속성)  # 표준정규분포 따르는 난수 생성
# low <= data < high
# a3 = np.random.randint(1,10,size=(10,)) # 1부터 10까지 1차원의 10개 데이터
# print(a3)
# a3 = np.random.randint(1,46,size=(6,)) # 1부터 46까지 1차원의 6개 데이터
# print(a3)
# a3 = np.random.randint(1,100,size=(2,3)) # 1부터 100까지 2행 3열의 데이터
# print(a3)
# a3 = np.random.randint(100,size=(2,3)) # low 값이 0인 경우
# print(a3)

# seed 값 : 난수 발생 위치를 고정
# np.random.seed(10)
# a3 = np.random.randint(10, size=(2,3))
# print(a3)
# a3 = np.random.randint(100, size=(2,3))
# print(a3)

# 변수 = np.random.normal([속성])
# 정규분포에서 표본추출한 난수를 발생
# 속성 loc : 정규분포의 평균 defalut 0
#     scale : 표준편차 defalut 1
#     size : shape 
# a3 = np.random.normal(loc=0,scale=1,size=(1000,))
# import matplotlib.pyplot as plt
# plt.hist(a3, bins=100)
# plt.show()

# np.random.rand(행수, 열수) : 0-1 사이의 균등분포형상으로 난수
# np.random.randn() : 가우시안 표준정규분포
# np.random.random([size]) : 0-1 균등분포형상으로 난수
# a3 = np.random.rand(3,2)
# print(a3)
# a3 = np.random.randn(3,2)
# print(a3)
# a3 = np.random.random(size=(3,2))
# print(a3)


# 파일 입출력
# text 형태로 저장 및 불러오기
# np.savetxt(파일명, 배열, 옵션)
# a1 = np.random.randint(0,10,size=(2,4))
# np.savetxt('data\\a1.csv', a1, delimiter=',')   # defalut 는 ,없는것

# np.loadtxt(파일명, 옵션)
# b1 = np.loadtxt('data\\a1.csv', delimiter=',', dtype=np.int)
# print(b1)

# binary 형태의 저장 및 불러오기
# np.save(파일명, 배열명)
# np.savez(파일명, 배열명1, 배열명2..)  => dictionary 형태로 저장
# np.savez(파일명, key1=배열명1, key2=배열명2..)
# a2 = np.ones((10,))
# print(a2)
# np.save('data\\aa1',a1)
# np.savez('data\\aa2',a1,a2)
# np.savez('data\\aa3',a1=a1, a2=a2)

# c1 = np.load('data\\aa1.npy')
# c2 = np.load('data\\aa2.npz')
# c3 = np.load('data\\aa3.npz')
# print(c1)
# print(c2)
# print(c3)
# print('npz파일의 키값 확인',c2.files)
# print(c2['arr_0'])
# print(c2['arr_1'])
# print('npz파일의 키값 확인',c3.files)
# print(c3['a1'])
# print(c3['a2'])

# li = [3.14,2,5,7,9,1] 
# a1 = np.array(li)
# print(a1)
# a1 = np.array(li, dtype=np.int)
# print(a1)
# a1 = np.array(li, dtype=np.string_)
# print(a1)

# 연산
# a1 = np.array([[1,2,3],[4,5,6]], np.float)
# print(a1)
# print(a1+a1)
# print(a1-a1)
# print(1/a1)

# 불린추출
# np.random.seed(10)
# names = np.array(['kim', 'park', 'lee', 'jung', 'kim', 'ji', 'yoo'])
# print(names)
# score = np.random.randint(0,100,(7,3))
# 각 이름이 score 의 행에 대응된다고 가정
# print(score)
# print(names=='kim') # [ True False False False False False False]
# print(score[names=='kim'])
# print(score[names=='kim',1:])
# print(score[names=='kim',1])    # 1차원으로 출력

# print(score)
# print(score[names!='kim'])
# print(score[~(names=='kim')])
# print('-'*30)
# print(score[(names=='kim')|(names=='ji')])
# and, or 사용X 
# &, | 사용

# 점수가 30 미만은 0으로
# print(score[score<30])
# score[score<30] = 0
# print(score)


# 2014년 시애틀 1월 강수량의 평균
# import pandas as pd
# data = pd.read_csv('data\\seattle.csv')
# print(data)
# data.info() # PRCP 가 강수량 컬럼
# rain = data['PRCP']
# print(rain)
# days = np.arange(365)
# print(days)
# chk = days<=30
# print(chk)
# jan = rain[chk]
# print(jan)
# print(np.mean(jan))

# reshape
# a1 = np.arange(15)
# print(a1)
# a1 = np.arange(15).reshape((3,5))
# print(a1)
# # a1 = np.arange(15).reshape((3,6))   # 데이터 개수가 동일하지 않으므로 error
# a2 = np.arange(15)
# print(a2)
# a2 = np.resize(a2, (3,5))
# print(a2)

# a1 = np.array(np.arange(16))
# print(a1)
# a1 = a1.reshape(2,4,2)
# print(a1)
# a1 = a1.reshape(4, -1)  # 행 4 정해주고 -1은 데이터수 맞추어 알아서 계산
# print(a1)
# a1 = a1.reshape(-1)
# print(a1)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,0,-1],[1,1,0]])
print(a)
b = b.T
print(b)
# 전치행렬
print(np.dot(a,b))  # 행렬곱

