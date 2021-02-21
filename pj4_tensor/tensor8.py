import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import random
import numpy as np
# mnist 손글씨 이미지 분류
# mnist = input_data.read_data_sets('../mnist/data', one_hot=True)
# print('train_set=',mnist.train)
# print('test_set=',mnist.test)
# print('train_set_size=',mnist.train.num_examples) # 55000
# print('test_set_size=',mnist.test.num_examples) # 10000
# print('train_data 5000번째 data',mnist.train.images[4999:5000])
# print('train_data 5000번째 data 정답',mnist.train.labels[4999:5000])
# plt.imshow(mnist.train.images[4999:5000].reshape(28,28),cmap='Greys',interpolation='nearest')
# plt.show()
# print('test_data 5000번째 data',mnist.test.images[4999:5000])
# print('test_data 5000번째 data 정답',mnist.test.labels[4999:5000])
# print('test_data 5000번째 data 차원',mnist.test.images[4999:5000].shape)
# plt.imshow(mnist.test.images[4999:5000].reshape(28,28),cmap='Greys',interpolation='nearest')
# plt.show()

# x = tf.placeholder(tf.float32, [None, 784])
# y = tf.placeholder(tf.float32, [None, 10])
# w = tf.Variable(tf.random_normal([784,10]))
# b = tf.Variable(tf.random_normal([10]))
# logits = tf.matmul(x,w)+b
# h = tf.nn.softmax(logits)
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y))
# # cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(h), axis=1))
# train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
# corr = tf.equal(tf.argmax(h,1), tf.argmax(y,1))
# acc = tf.reduce_mean(tf.cast(corr,tf.float32))
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(5001):
#         batch_x, batch_y = mnist.train.next_batch(100)
#         sess.run(train, feed_dict={x:batch_x, y:batch_y})
#         if i%500 == 0:
#             # print(sess.run(acc,feed_dict={x:mnist.train.images, y:mnist.train.labels}))
#             print(sess.run(cost,feed_dict={x:mnist.train.images, y:mnist.train.labels}))
#     # 평가
#     print('정확도=',sess.run(acc, feed_dict={x:mnist.test.images, y:mnist.test.labels}))

#     # 예측
#     r = random.randint(0,mnist.test.num_examples-1) # r = 0~9999
#     print('실제정답:', sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))
#     print('예측값', sess.run(tf.argmax(h,1), feed_dict={x:mnist.test.images[r:r+1]}))
#     plt.imshow(mnist.test.images[r:r+1].reshape(28,28), cmap='Greys', interpolation='nearest')
#     plt.show()
# =================================================================================================

# 이진분류 - 당뇨병 데이터
data = np.loadtxt('data/diabetes.csv', delimiter=',')
print(data.shape) # (759, 9)
train_x = data[:569,:-1]
train_y = data[:569,-1:]
test_x = data[569:,:-1]
test_y = data[569:,-1:]
x = tf.placeholder(tf.float32, [None,8])
y = tf.placeholder(tf.float32, [None,1])
w = tf.Variable(tf.random_normal([8,1]))
b = tf.Variable(tf.random_normal([1]))
logits = tf.matmul(x,w)+b
h = tf.sigmoid(logits)
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y))
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5001):
        sess.run(train, feed_dict={x:train_x, y:train_y})
        if i%100==0:
            print(sess.run(cost, feed_dict={x:train_x, y:train_y}))
    # 예측
    # print(sess.run(h,feed_dict={x:test_x}))
    pred = tf.cast(h>0.5, tf.float32)
    print('예측값=', sess.run(pred,feed_dict={x:test_x}))
    # 평가
    acc = tf.reduce_mean(tf.cast(tf.equal(pred, y), tf.float32))
    print('정확도=',sess.run(acc,feed_dict={x:test_x, y:test_y}))

