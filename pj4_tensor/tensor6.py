from operator import delitem
from sklearn.datasets import load_diabetes
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
diabetes = load_diabetes()
# print(diabetes.data.shape)  # (442, 10)
# print(diabetes.target.shape)    # (442,)
# print(diabetes.data[:3])
# print(diabetes.target[:3])

# xdata = diabetes.data[:,2]
# ydata = diabetes.target
# print('xdata=',xdata)
# print('ydata=',ydata)
# plt.plot(xdata, ydata,'o')
# plt.show()
# print('xdata=',xdata[:10])
# print('ydata=',ydata[:10])

# h = wx + b
# w, b 초기화 (임의로 설정)
# w = 1.0
# b = 1.0
# h = xdata[0]* w + b 
# print('예측값 h=',h)
# print('정답 ydata=',ydata[0])

# 경사하강법 : 모델이 데이터를 잘 표현할 수 있도록
# 기울기를 사용하여 모델을 조금씩 조정하는 알고리즘
# w를 업데이트
# winc = w + 0.1
# hinc = xdata[0] * winc + b
# print('예측값 hinc=',hinc)
# wrate = (hinc-h)/(winc-w)
# print('wrate=',wrate) # =xdata[0]
# wnew = w + wrate
# print('wnew=',wnew)

# 절편 업데이트
# binc = b + 0.1
# hinc = hinc = xdata[0] * w + binc
# print('절편값의 변화에 따른 hinc',hinc)
# brate = (hinc-h)/(binc-b)
# print('brate=',brate)   # 1.0
# bnew = b + brate
# print('bnew',bnew)
# =====================================================


# 오차역전파 : 예측값과 정답의 차이를 이용하여 x와 b를 업데이트
# 오차가 연이어 전파되는 모습
# err = ydata[0] - h
# winc = w + 0.1
# hinc = xdata[0] * winc + b
# wrate = (hinc-h)/(winc-w)
# binc = b + 0.1
# hinc = hinc = xdata[0] * w + binc
# brate = (hinc-h)/(binc-b)
# wnew = w + wrate * err
# bnew = b + brate * err
# print('wnew=',wnew,'bnew=',bnew)
# # 두번째 샘플에 적용
# h = xdata[1]*wnew+bnew
# print('예측값=',h,'정답=',ydata[1])
# err = ydata[1]- h
# wrate = xdata[1]
# wnew = wnew + wrate * err
# bnew = bnew + brate * err
# print('wnew=',wnew,'bnew=',bnew)
# for xi,yi in zip(xdata,ydata):
#     h = xi*w + b
#     err = yi - h
#     wrate = xi
#     w = w + wrate*err
#     b = b + 1*err
#     print('w=',w,'b=',b)    # w= 587.8654539985689 b= 99.40935564531424
# plt.plot(xdata,ydata,'o')
# left = -0.1*w+b
# right = 0.2*w+b
# plt.plot([-0.1,0.2],[left,right])
# plt.show()

# epoch: 한 단위의 작업을 진행하는 것
# 여러 epoch 반복
# for i in range(1001):
#     for xi,yi in zip(xdata,ydata):
#         h = xi*w + b
#         err = yi - h
#         wrate = xi
#         w = w + wrate*err
#         b = b + 1*err
#         print('w=',w,'b=',b) 
# plt.plot(xdata,ydata,'o')
# left = -0.1*w+b
# right = 0.2*w+b
# plt.plot([-0.1,0.2],[left,right])
# plt.show()
# ==========================================

# 분류 -> iris
# data = np.loadtxt('data/iris1.csv',delimiter=',',skiprows=1)
# print(data)
# print(data.shape) # (150, 7)
# # 70% data -> 학습, 30% data -> 검증
# np.random.shuffle(data)
# train_x, train_y = data[:105,:4], data[:105,4:]
# # print(train_x.shape) # (105, 4) 학습용데이터
# # print(train_y.shape) # (105, 3) 학습용데이터 정답
# test_x, test_y = data[105:,:4], data[105:,4:]
# # print(test_x.shape) # (45, 4) 검증용데이터
# # print(test_y.shape) # (45, 3) 검증용데이터 정답
# # print(test_y)
# x = tf.placeholder(tf.float32,[None,4])
# y = tf.placeholder(tf.float32,[None,3])
# w = tf.Variable(tf.random_normal([4,3]))
# b = tf.Variable(tf.random_normal([3]))
# logits = tf.matmul(x,w)+b   # 분류 문제일 때 추가
# h = tf.nn.softmax(logits)
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y))
# train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     # 학습하기
#     for i in range(1001):
#         sess.run(train,feed_dict={x:train_x, y:train_y})
#         if i%100 == 0:
#             print(sess.run(cost,feed_dict={x:train_x, y:train_y}))
#     # 검증하기
#     pred = sess.run(h,feed_dict={x:test_x})
#     corr = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
#     acc = tf.reduce_mean(tf.cast(corr, tf.float32))
#     print('정확도=',sess.run(acc,feed_dict={x:test_x, y:test_y}))
# ==================================================================


# wine-quality
# https://archive.ics.uci.edu/ml/machine-learning-databases
data = np.loadtxt('data/wine.csv',delimiter=';',skiprows=1)
# print(data)
# print(data.shape) # (4898, 12)
np.random.shuffle(data)
train_x, train_y = data[:3429,:11], data[:3429,11:]
test_x, test_y = data[3429:,:11], data[3429:,11:]
# print(train_x.shape) # (3429, 11)
# print(train_y.shape) # (3429, 1) => onehot으로 변경해야해
x = tf.placeholder(tf.float32, [None,11])
y = tf.placeholder(tf.int32, [None,1])
onehot = tf.one_hot(y,11)   # wine_quaility -> 0 ~ 10 -> 11가지
onehot2 = tf.reshape(onehot,[-1,11])  # 차원 축소 (3 -> 2차원)
w = tf.Variable(tf.random_normal([11,11]))
b = tf.Variable(tf.random_normal([11]))
logits = tf.matmul(x,w)+b
h = tf.nn.softmax(logits)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=onehot2))
train = tf.train.GradientDescentOptimizer(0.0005).minimize(cost)

corr = tf.equal(tf.argmax(h,1), tf.argmax(onehot2,1))
acc = tf.reduce_mean(tf.cast(corr, tf.float32))

with tf.Session() as sess:
    # print(sess.run(y, feed_dict={y:train_y}))
    # print(sess.run(onehot, feed_dict={y:train_y}))
    # print(sess.run(onehot2, feed_dict={y:train_y}))
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        sess.run(train, feed_dict={x:train_x, y:train_y})
        if i%100 == 0:
            print('cost=',sess.run(cost, feed_dict={x:train_x, y:train_y}))
            print('정확도=',sess.run(acc,feed_dict={x:test_x, y:test_y}))