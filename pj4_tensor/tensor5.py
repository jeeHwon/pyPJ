import tensorflow as tf
import numpy as np

# 선형회귀 : 지도학습에서 수치를 예측

# water.csv 파일 
# (전월)총 정수기 대여개수, 10년이상 노후 정수기 대수, AS 시간
# 다음달 AS 시간을 예측하고 이에대한 신규인력을 채용하고자 할 때.

data = np.loadtxt('data/water.csv', delimiter=',',skiprows=1) 
# print(data)
xdata = data[:,1:-1]
ydata = data[:,-1:]
print(xdata.shape)
print(ydata.shape)

# x = tf.placeholder(tf.float32, [None,2])
# y = tf.placeholder(tf.float32, [None,1])
# w = tf.Variable(tf.random_normal([2,1]))
# b = tf.Variable(tf.random_normal([1]))
# h = tf.matmul(x,w)+b
# cost = tf.reduce_mean(tf.square(y-h))
# train = tf.train.GradientDescentOptimizer(0.00000000001).minimize(cost)

# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(10001):
#         sess.run(train, feed_dict={x:xdata, y:ydata})
#         if i%100 == 0:
#             print(sess.run(cost, feed_dict={x:xdata, y:ydata}))


# # 월말 총 대여수 30,000대, 그 중 노후 정수기 70,000대로 집계, AS 시간 예측
#     result = sess.run(h, feed_dict={x:[[70000,230000]]})[0][0]
#     print('예측값=',result)
# =======================================================================


# 다중분류
# data -> https://archive.ics.uci.edu/ml/machine-learning-databases
data = np.loadtxt('data/zoo/zoo.csv', delimiter=',')
# print(data.shape) # (101, 17)
xdata = data[:, :-1]
ydata = data[:, -1:]
# print(xdata.shape) # (101, 16) -> 데이터
# print(ydata.shape) # (101, 1)  -> 레이블
x = tf.placeholder(tf.float32,[None, 16])
y = tf.placeholder(tf.int32,[None, 1]) # 0~6 -> one_hot
onehot = tf.one_hot(y,7)
onehot2 = tf.reshape(onehot,[-1,7]) # 3차원 -> 2차원
# w X x + b = y 
# [None, 16] X [?, ?] = [None, 7]
# => [?, ?] = [16, 7]
w = tf.Variable(tf.random_normal([16,7]))
b = tf.Variable(tf.random_normal([7]))
logits= tf.matmul(x,w)+b
h = tf.nn.softmax(logits)   # 다중분류 시 소프트맥스 알고리즘
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=onehot2))
train = tf.train.GradientDescentOptimizer(0.7).minimize(cost)
with tf.Session() as sess:
    # print(sess.run(x,feed_dict={x:xdata}))
    # print(sess.run(y,feed_dict={y:ydata}))
    # print('*'*30)
    # print(sess.run(onehot, feed_dict={y:ydata}))
    sess.run(tf.global_variables_initializer())
    # print('학습전 예측값\n',sess.run(h, feed_dict={x:xdata}))
    # print(sess.run(tf.argmax(h,1), feed_dict={x:xdata}))
    # print(sess.run(tf.equal(tf.argmax(h,1), tf.argmax(onehot2,1)), feed_dict={x:xdata,y:ydata}))
    # print(sess.run(tf.cast(tf.equal(tf.argmax(h,1), tf.argmax(onehot2,1)), tf.float32), feed_dict={x:xdata,y:ydata}))
    # print('학습전 정확도=\n',
    #     sess.run(tf.reduce_mean(tf.cast(tf.equal(tf.argmax(h,1), tf.argmax(onehot2,1)), tf.float32)), feed_dict={x:xdata,y:ydata}))
    
    for i in range(3001):
        sess.run(train, feed_dict={x:xdata, y:ydata})
        if i%100 == 0:
            print(sess.run(cost, feed_dict={x:xdata, y:ydata}))

    # 평가하기
    correct = tf.equal(tf.argmax(h,1), tf.argmax(onehot2,1)) # True, False..
    accuracy = tf.reduce_mean(tf.cast(correct,tf.float32))
    print('정확도=',sess.run(accuracy,feed_dict={x:xdata, y:ydata}))

    # 예측하기
    print(sess.run(h, feed_dict={x:[[0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0]]}))
    print(sess.run(tf.argmax(h,1), feed_dict={x:[[0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0]]}))