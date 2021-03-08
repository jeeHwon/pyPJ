# 퍼셉트론 : 다수의 신호(0 or 1)를 입력받아 하나의 신호를 출력
# 가중치가 클수록 해당 신호가 중요함을 나타냄
# 신경망의 기원
# 가중치를 설정하는 작업을 사람이
# 신경망 : 가중치의 적절한 값을 데이터로부터 자동으로 학습

# and 게이트
import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.5
    temp = np.dot(w, x) + b
    print(temp)
    if temp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    temp = np.dot(w, x) + b
    # print(temp)
    if temp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    temp = np.dot(w, x) + b
    # print(temp)
    if temp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    r1 = NAND(x1, x2)
    r2 = OR(x1, x2)
    y = AND(r1, r2)
    return y


if __name__ == '__main__':
    for xx in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        # y = AND(xx[0], xx[1])
        # y = OR(xx[0], xx[1])
        # y = NAND(xx[0], xx[1])
        y = XOR(xx[0], xx[1])
        # print(xx, '-->', y)

import matplotlib.pyplot as plt


def stepFunction(x):
    return np.array(x > 0, np.int)


def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-5, 5, 0.1)
print(x)
y = stepFunction(x)
y2 = sigmoid(x)
plt.plot(x, y)
plt.plot(x, y2)
plt.show()