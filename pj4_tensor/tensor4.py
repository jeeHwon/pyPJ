import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# xdata = [1,2,3]
# ydata = [1,2,3]
# w = tf.Variable(tf.random_normal([1]))
# b = tf.Variable(tf.random_normal([1]))

# h = w * xdata + b
# cost = tf.reduce_mean(tf.square(h-ydata))
# train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(2001):
#         if i%100==0:
#             print(i, sess.run(cost), sess.run(w), sess.run(b))
#         sess.run(train)


# data = np.loadtxt('data/cars.csv', unpack=True, delimiter=',', skiprows=1)
# # print(data)
# print(data[0]) # speed
# print(data[1]) # distance
# plt.plot(data[0], data[1], 'o')
# # plt.show()
# x = tf.placeholder(tf.float32)
# y = tf.placeholder(tf.float32)
# w = tf.Variable(tf.random_uniform([1],-1,1))
# b = tf.Variable(tf.random_uniform([1],-1,1))
# h = w * x + b
# cost = tf.reduce_mean(tf.square(y-h))
# train = tf.train.GradientDescentOptimizer(0.001).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(2001):
#         sess.run(train, feed_dict={x:data[0], y:data[1]})
#         if i%100 == 0:
#             print(sess.run([cost,w,b], feed_dict={x:data[0], y:data[1]}))
#     # x가 20일 때 제동거리 예측        
#     # print('예측값', sess.run(h, feed_dict={x:20}))
#     # x가 0,30일 때 제동거리 예측        
#     result = sess.run(h, feed_dict={x:[0,30]})
#     print(result)
# plt.plot([0,30], result)
# plt.show()

# x = tf.placeholder(tf.float32)
# y = tf.placeholder(tf.float32)
# w = tf.Variable([0.5], tf.float32)
# b = tf.Variable([0.5], tf.float32)
# h = w * x + b
# cost = tf.reduce_mean(tf.square(y-h))
# train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(2001):
#         sess.run(train, feed_dict={x:[1,2,3,4], y:[0,-1,-2,-3]})
#         if i%100 ==0:
#             print(sess.run(cost, feed_dict={x:[1,2,3,4], y:[0,-1,-2,-3]}))

# cost 함수 시각화
# x = [1,2,3]
# y = [1,2,3]
# w = tf.placeholder(tf.float32)
# h = w * x
# cost = tf.reduce_mean(tf.square(h-y))
# with tf.Session() as sess:
#     costlist=[]
#     wlist=[]
#     for i in range(-40,60):     # w = -4~6 0.1씩 증가
#         temp = i * 0.1
#         tempcost, tempw = sess.run([cost,w], feed_dict={w:temp})
#         costlist.append(tempcost)
#         wlist.append(tempw)
# plt.plot(wlist, costlist)
# plt.show()

xdata = np.random.rand(100,1)   # 0~1 사이의 값
# print(x)
xdata = xdata * 4 -2  # -2~2 사이의 값
ydata = 3 * xdata - 2
ydata = ydata + np.random.randn(100,1)  # 노이즈 추가
# plt.plot(x,y,'o')
# plt.show()
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1]),tf.float32)
b = tf.Variable(tf.random_normal([1]),tf.float32)
h = w * x + b
cost = tf.reduce_mean(tf.square(h-y))
train = tf.train.GradientDescentOptimizer(0.005).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(501):
        sess.run(train, feed_dict={x:xdata, y:ydata})
        if i%100==0:
            tempcost,tempw,tempb=sess.run([cost,w,b],feed_dict={x:xdata,y:ydata})
            print(tempcost,tempw,tempb)
            temph=sess.run(h,feed_dict={x:xdata})
            plt.plot(xdata,ydata,'o')
            plt.plot(xdata,temph)    #모델
            plt.show()
    result = sess.run(h, feed_dict={x:[-10,-20]})
    print('예측값:',result)



