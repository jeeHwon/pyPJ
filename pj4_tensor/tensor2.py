import tensorflow as tf
import numpy as np

# 경고 메시지 무시
import os
from tensorflow.python.ops.variables import global_variables_initializer
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# a = tf.constant(120, name='aa')
# b = tf.constant(5, name='bb')
# c = tf.constant(100)
# # print(a)
# # print(b)
# # print(c)
# v = tf.Variable(0, name='v')
# op1 = a + b + c
# op2 = tf.assign(v, op1)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(op2))
#     result = sess.run([a,b,c,op2])
#     print(result)
#     print(type(result), type(result[0]))

# 구구단 출력
# dan = tf.placeholder(tf.int32)
# i = tf.placeholder(tf.int32)
# op1 = dan * i
# with tf.Session() as sess:
#     # print(sess.run(op1, feed_dict={dan:5, i:[1,2,3,4,5,6,7,8,9]}))
#     result = sess.run([dan, i, op1], feed_dict={dan:5, i:[1,2,3,4,5,6,7,8,9]})
#     # print(result)
#     # print(result[0], result[1], result[2])
# for j in range(len(result[1])):
#     print('{} * {} = {}'.format(result[0], result[1][j], result[2][j]))

# 행렬차원 변환
# a = tf.constant([1,2,3,4,5,6,7,8,9,10,11,12])
# b = tf.constant([[1,1],[2,2],[3,3],[4,4]])
# with tf.Session() as sess:
#     print(sess.run(tf.reshape(a, (3,4))))
#     print(sess.run(tf.reshape(a, (3,2,-1))))
#     print(sess.run(tf.reshape(b, (-1,4))))

# 행렬곱셉
# a = tf.constant([[1.,2.]])
# b = tf.constant([[3.],[4.]])
# print(a, a.get_shape())
# print(b, b.get_shape())
# op1 = tf.matmul(a,b)
# with tf.Session() as sess:
#     print(sess.run(op1))

# 행렬 곱셉 위한 차원변환
# a = tf.constant([[1,2,3],[4,5,6]])
# b = tf.constant([1,0,1])
# print(a, a.get_shape())    #(2,3)
# print(b, b.get_shape())    #(3,)
# bb = tf.reshape(b,(3,-1))
# print(bb, bb.get_shape())    #(3,1)
# op1 = tf.matmul(a,bb)
# with tf.Session() as sess:
#     print(sess.run(bb))
#     print(sess.run(op1))

# tf.case(): 데이터타입 변환
# x = tf.constant([1.,2.,3.])
# print(x)
# y = tf.constant([True, False, True, False])
# print(y)
# with tf.Session() as sess:
#     print(sess.run(tf.cast(x, tf.int32)))
#     print(sess.run(tf.cast(y, tf.int32)))
#     print(sess.run(tf.reduce_mean(tf.cast(y, tf.int32))))   # 0
#     print(sess.run(tf.reduce_mean(tf.cast(y, tf.float32)))) # 0.5

# 상수생성
# z1 = tf.zeros([3,4,5])
# z2 = tf.zeros_like([3,4,5])
# f1 = tf.fill([2,3],7)
# f2 = tf.constant(7, shape=[2,3])
# with tf.Session() as sess:
#     print(sess.run(z1))
#     print('-'*30)
#     print(sess.run(z2))
#     print('-'*30)
#     print(sess.run(f1))
#     print('-'*30)
#     print(sess.run(f2))

# 기본형태 y = w*x + b
# xdata = np.random.randn(5,10)
# print(xdata)
# wdata = np.random.randn(10,1)
# print(wdata)
# x = tf.placeholder(tf.float32, shape=(5,10))
# w = tf.placeholder(tf.float32, shape=(10,1))
# b = tf.fill((5,1), -1.)
# y = tf.matmul(x,w) + b
# op1 = tf.matmul(x, w)
# with tf.Session() as sess:
#     print(sess.run(y, feed_dict={x:xdata, w:wdata}))

# tf.argmax(): 가장 큰 값을 찾아 인덱스 반환
# a = tf.constant([10,100,1,1000])
# b = tf.constant([[10,100,1],[11,21,31],[0,80,50]])
# with tf.Session() as sess:
#     print('인덱스갯수(차원)', sess.run(tf.rank(a)))
#     print('최대값 위치', sess.run(tf.argmax(a)))
#     print('최소값 위치', sess.run(tf.argmin(a)))
    # print('인덱스갯수(차원)', sess.run(tf.rank(b)))
    # print(sess.run(b))
    # print('최대값 위치(열방향)', sess.run(tf.argmax(b)))
    # print('최대값 위치(열방향)', sess.run(tf.argmax(b,0)))
    # print('최대값 위치(행방향)', sess.run(tf.argmax(b,1)))

# 행방향으로 가장 큰 값의 위치 출력
# a = tf.constant([[5,10,17],[4,50,6]])
# with tf.Session() as sess:
#     print(sess.run(a))
#     print('최대값 위치', sess.run(tf.argmax(a,1)))

# onehot : 사람이 이해할수 있는 데이터를 컴퓨터에 입력 시키는 방법 ex 0: 10000 / 3: 00010 
# a = np.array([0,1,2,3,4,5,6,7,8,9])
# print(a)
# b = np.array([0,1,2,0,1,1,2,2,0,1])
# print(b)
# x = tf.placeholder(tf.int32)
# y = tf.placeholder(tf.int32)
# onehot_x = tf.one_hot(x,10) # 차원증가
# onehot_x2 = tf.reshape(onehot_x, shape=[-1])    # 차원축소
# onehot_y = tf.one_hot(y,3)
# argmax_y = tf.argmax(onehot_y, 1)
# with tf.Session() as sess:
#     # print(sess.run(x, feed_dict={x:a}))
#     print('x=\n',sess.run(onehot_x, feed_dict={x:a}))
#     print('x=\n',sess.run(onehot_x2, feed_dict={x:a}))
#     print('y=\n',sess.run(onehot_y, feed_dict={y:b}))   # 원핫형태
#     print('y=\n',sess.run(argmax_y, feed_dict={y:b}))   # 원래형태

# r에서 iris 데이터를 받아 현재 프로젝트의 data 폴더내에 iris.csv로 넣기
# setosa     -> 0 -> 1,0,0  
# versicolor -> 1 -> 0,1,0
# virginica  -> 2 -> 0,0,1

# 과제) iris1.csv 데이터를 읽어 다음을 진행하시오
# 1) 앞쪽 4개의 모든 열은 xdata, 3개의 열은 ydata에 넣으시오
iris = np.loadtxt('data/iris1.csv', delimiter=',', skiprows=1, dtype=np.dtype)
xdata = np.array(iris[:,0:4])
ydata = np.array(iris[:,4:7])
# print(iris)
# print(xdata)
# print(ydata)

# 2) 실행 시에 x에 xdata, y에 ydata 값을 넣어서 원래의 값으로 복원하여 출력하시오
x = tf.placeholder(tf.float32, [150,4])
y = tf.placeholder(tf.float32, [150,3])
argmax_xy = tf.argmax(y,1)
with tf.Session() as sess:
    sess.run(x, feed_dict={x:xdata})
    print(sess.run(argmax_xy, feed_dict={y:ydata}))

