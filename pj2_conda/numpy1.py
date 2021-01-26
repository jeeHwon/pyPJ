import numpy as np

# Numerical Python 과학계산, 데이터 분석시 사용
# print(np.__version__)
# np.info(항목) 도움말
# np.info(np.array)

# 기본 배열
# 넘파이 배열 생성 - 같은 종류의 데이터를 담는 다차원 배열
# 변수 = np.array(list [,속성])

# li = [1,2,3,4,5]
# a1 = np.array(li)
# print(li)       # [1, 2, 3, 4, 5]
# print(a1)       # [1 2 3 4 5] 넘파이 배열은 comma로 표시 X
# print(a1.shape) # (5,) 튜플형태로 출력(행수, )
# print(a1.dtype) # int32
# print(type(a1)) # <class 'numpy.ndarray'>
# print(a1.ndim)  # 1 배열의 차원
# print('-'*100)

# a2 = np.array(li, dtype=np.float64)
# print(a2)
# print(a2.dtype)
# print('-'*100)

# a3 = np.array([1,2,3.,4,5]) # 하나의 데이터타입을 취급하므로 모두 float 형태로 변환
# print(a3)
# print('-'*100)

# 2차원
# d2 = np.array([[1,2,3],[4,5,6]])
# print(d2)
# print(d2.shape)

# 3차원
# d3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(d3)
# print(d3.shape)

# 초기화 함수
# 변수 = np.zeros(shpae,[속성])
# z1 = np.zeros((2,3))
# print(z1)
# z2 = np.ones((2,3))
# print(z2)
# z3 = np.full((2,3),7)
# print(z3)
# z4 = np.empty((2,3))    # 기존 메모리에 남아 있는 값(랜덤이라 생각하자)
# print(z4)
# print('-'*100)

# 단위행렬
# a1 = np.eye(3)
# print(a1)
# li = [[1,2,3,4],[5,6,7,8]]
# print(li)
# a1 = np.ones_like(li)
# print(a1)
# a1 = np.zeros_like(li)
# print(a1)
# a1 = np.full_like(li, 3.5) # 소숫점 버리는게 default
# a1 = np.full_like(li, 3.52, dtype=np.float64)
# print(a1)
# a1 = np.empty_like(li)
# print(a1)

# 데이터 입출력
# 변수 = loadtxt(파일명 , 속성)
# data = np.loadtxt('data/d1.txt')
# print(data)
# print(data.shape)
# 데이터를 수직으로 읽기
# data = np.loadtxt('data/d1.txt', unpack=True)
# print(data)
# print(data.shape)   # (2, 3)
# print(type(data))   # <class 'numpy.ndarray'>
# print(data[0])      # [1. 2. 3.]
# print(data[1])      # [10. 20. 30.]
# print(data[0][2])   # 3.0
# print('-'*100)

# comma로 구분되어 있는 파일 읽기
# data = np.loadtxt('data/d2.txt', delimiter=',')
# print(data)
# data = np.loadtxt('data/d2.txt', delimiter=',', unpack=True)
# print(data)

# 첫째줄에 data name 삽입되어 있는 파일 읽기
# data = np.loadtxt('data/d3.txt', delimiter=',', skiprows=1)
# print(data)

# arange (파이썬 range 함수의 numpy 버전)
# print(np.arange(10))
# print(np.arange(10).astype(np.float))   # 데이터형 변환
# a1 = np.arange(15)
# print(a1)
# print(a1[5])
# print(a1[5:8])
# a1[5:8] = 99
# print(a1)
# b = a1[5:8]
# print('b=', b)
# b[1] = 100           # 넘파이에서 배열의 조각은 원본의 뷰
# print('b=', b)
# print('a1=', a1)     # a의 일부를 b에 할당해서 b 변경시 a도 변경
# c = a1[5:8].copy()   # 원본 배열의 복사본을 할당
# print('c=', c)
# c[2] = 101
# print('a1=', a1)
# print('b=', b)
# print('c=', c)

# 특정 데이터 인덱스 접근방법
# a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a1[2])        # [7 8 9]
# print(a1[2][1])     # 8
# print(a1[2,1])      # 윗줄과 같은코드
# print('a1[:2]\n',a1[:2])       #  [[1 2 3] [4 5 6]]
# print('a1[:2,1:]\n',a1[:2,1:]) #  [[2 3] [5 6]]
# print(a1[2][0])                # 7
# print(a1[2][:1])               # [7]

# 데이터 입출력
# 1.save(파일명, numpy배열) binary 형태로 저장 -> .npy
# a0 = np.zeros((4,3))
# print(a0)
# a1 = np.ones((2,3))
# print(a1)
# a7 = np.full((5,2),7)
# print(a7)
# np.save('data/a0',a0)
# np.save('data/a1',a1)
# np.save('data/a7',a7)

# 2.savez(파일명, 넘파이배열1, 넘파이배열2..) 두개이상의 ndarray를 binary 형태로 저장 -> .npz
# np.savez('data/all',a0, a1, a7)

# 3.savetxt() text 형태로 저장

# 변수 = np.load(파일명)
# c0 = np.load('data/a0.npy')
# print(c0)
# c1 = np.load('data/a1.npy')
# print(c1)
c_all = np.load('data/all.npz')
print(c_all)        # <numpy.lib.npyio.NpzFile object at 0x00000211A0B7D550>
print(c_all.files)  # ['arr_0', 'arr_1', 'arr_2'] 여러개 저장시 dictionary 형태로 저장
print(c_all['arr_0'])
print(c_all['arr_1'])
print(c_all['arr_2'])




