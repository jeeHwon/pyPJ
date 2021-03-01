import tensorflow as tf
import numpy as np
import math

# 경고 메시지 무시
import os
from tensorflow.python.ops.variables import global_variables_initializer
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 과제 1
print('='*30, '과제1', '='*30)
data = np.loadtxt('data/water.csv', delimiter=',',skiprows=1) 
xdata = data[:,1:-1]
ydata = data[:,-1:]

x = tf.placeholder(tf.float32, [None,2])
y = tf.placeholder(tf.float32, [None,1])
w = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))
h = tf.matmul(x,w)+b
cost = tf.reduce_mean(tf.square(y-h))
train = tf.train.GradientDescentOptimizer(0.00000000001).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5001):
        sess.run(train, feed_dict={x:xdata, y:ydata})
        # if i%100 == 0:
        #     print(sess.run(cost, feed_dict={x:xdata, y:ydata}))
    print('cost =',sess.run(cost, feed_dict={x:xdata, y:ydata}))
    print('기울기 =',sess.run(w, feed_dict={x:xdata, y:ydata}))
    print('절편 =',sess.run(b, feed_dict={x:xdata, y:ydata})[0])

    as_time = sess.run(h, feed_dict={x:[[80000,270000]]})[0][0]
    as_people = math.ceil(as_time / (8 * 20))
    print(f'AS 예측시간 : {as_time}시간')
    print(f'필요 AS 기사 인원수 : {as_people}명')


# 과제 2
print('='*30, '과제2', '='*30)
iris = np.loadtxt('data/iris1.csv',delimiter=',',skiprows=1)
np.random.shuffle(iris)
train_x, train_y = iris[:105,:4], iris[:105,4:]
test_x, test_y = iris[105:,:4], iris[105:,4:]
x = tf.placeholder(tf.float32,[None,4])
y = tf.placeholder(tf.float32,[None,3])
w = tf.Variable(tf.random_normal([4,3]))
b = tf.Variable(tf.random_normal([3]))
logits = tf.matmul(x,w)+b   
h = tf.nn.softmax(logits)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits,labels=y))
train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1001):
        sess.run(train,feed_dict={x:train_x, y:train_y})
    pred = sess.run(h,feed_dict={x:test_x})
    corr = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
    acc = tf.reduce_mean(tf.cast(corr, tf.float32))
    print('정답율=',sess.run(acc,feed_dict={x:test_x, y:test_y}))
