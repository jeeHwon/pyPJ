import numpy as np
# 과제 water.csv를 넘파이 배열(data)로 읽어
# x에 total과 old값 할당 y에 as_time 할당

data = np.loadtxt('data/water.csv', delimiter=',', skiprows=1)
print(data)
x = data[:, :2]
print(x)
y = data[:, 2]
print(y)
