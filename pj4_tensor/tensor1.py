import tensorflow as tf
# print(tf.__version__)

# 경고 메시지 무시
import os

from tensorflow.python.ops.variables import global_variables_initializer
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# hello = tf.constant("hello, Tensorflow")
# sess = tf.Session()
# print(sess.run(hello))
# sess.close()

# 노드 : 텐서(다차원배열)를 입력받아 텐서를 출력
# 상수 노드 : 변경할 수 없는 고정된 값
# tf.constant(데이터, dtype=데이터유형, shape=데이터차수, name=텐서명)

# node1 = tf.constant(3, tf.float32)
# node2 = tf.constant(4)
# print(node1)
# print(node2)

# tesorflow는 성능을 향상시키기 위해 정의와 실행을 분리
# Session() : 세션객체 생성
# 세션변수.run(노드[feed_dict=데이터]) : 노드를 실행
# sess = tf.Session()
# print(sess.run(node1))
# print(sess.run(node2))
# print(sess.run([node1, node2]))
# sess.close()    # 세션종료

# Operation : 값을 저장하는 노드를 연결하는 것, 그 자체로 노드
# node1 = tf.constant(3)
# node2 = tf.constant(4)
# node3 = node1 + node2
# node4 = tf.subtract(node1, node2)
# print(node1)
# print(node2)
# sess = tf.Session()
# print(sess.run([node1,node2]))
# print(sess.run([node3,node4]))
# sess.close()

# a = tf.constant(5)
# b = tf.constant(2)
# c = tf.constant(3)
# d = tf.multiply(a,b)
# e = tf.add(c,b)
# f = tf.subtract(d,e)
# with tf.Session() as sess:
#     r1 = sess.run(c)
#     r2 = sess.run([a,b,c,d,e,f])
# print(r1)
# print(r2)
# print(type(r1))
# print(type(r2[0]))  # 리스트의 각 항목데이터는 넘파이

# 변수1) Variable(데이터,데이터형태,이름) 변수는 초기화 작업후에 사용한다
# 변수초기화 tf.global_variables)initializer()
# w = tf.Variable([.3])
# with tf.Session() as sess:
#     sess.run(global_variables_initializer())
#     print(sess.run(w))

# tf.assign(노드,데이터,이름) : 변수의 값을 변경하는 함수
# a = tf.constant(5, name='aa')
# b = tf.constant(2, name='bb')
# c = tf.constant(3, name='cc')
# d = tf.multiply(a,b, name='op1')
# e = tf.add(c,b)
# f = tf.subtract(d,e)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# state = tf.Variable(0)
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(5):
#         sess.run(update)
#         print(sess.run(state))

# 변수2) tf.placeholder(데이터타입,shape=차원,name=이름) 초기값을 입력하지 않고 정의
# 세션에서 값을 넣어서 실행
# a = tf.placeholder(tf.int32, [3])
# b = tf.constant(2)
# op1 = a*b
# with tf.Session() as sess:
#     print(sess.run(op1, feed_dict={a:[10,20,30]}))
#     print(sess.run(op1, feed_dict={a:[4,5,6]}))

# v = tf.placeholder(tf.int32, [None])
# b = tf.constant(11)
# op1 = v*b
# with tf.Session() as sess:
#     print(sess.run(op1, feed_dict={v:[10]}))
#     print(sess.run(op1, feed_dict={v:[4,5,6]}))
#     print(sess.run(op1, feed_dict={v:[4,5,6,7,8]}))

# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# op1 = tf.add(a,b)
# with tf.Session() as sess:
#     print(sess.run(op1, feed_dict={a:10,b:5}))
#     print(sess.run(op1, feed_dict={a:[1,2],b:[3,4]}))

# 정규분포 따르는 난수 생성 tf.random_normal(shape,mean,stddev)
# i = tf.random_normal((1,5),0,1)
# v = tf.Variable(i)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(v))

# 차수변경
# a = tf.constant([1,2,3,4,5,6,7,8,9])
# b = tf.constant([[1,1],[2,2],[3,3],[4,4]])
# with tf.Session() as sess:
#     print(sess.run(a))
#     print(sess.run(tf.reshape(a,(3,3))))
#     print(sess.run(b))
#     print(sess.run(tf.reshape(b,[4,-1])))
#     print(sess.run(tf.reshape(b,[-1])))

# 실행시 값을 입력 받아 해당 구구단을 출력
# inputNum = input("숫자를 입력하세요: ")
# x = tf.placeholder(tf.int32)
# opNum = tf.constant([1,2,3,4,5,6,7,8,9])
# op_mul = tf.multiply(x,opNum)
# with tf.Session() as sess:
#     print(sess.run(op_mul, feed_dict={x: inputNum}))

# 과제: 실행시 값을 입력 받아 해당 구구단을 출력
inputNum = input("구구단 몇단을 실행할까요?: ")
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
op1 = tf.multiply(a,b)
with tf.Session() as sess:
    print("구구단 {}단: ".format(inputNum),sess.run(op1, feed_dict={a:inputNum,b:[1,2,3,4,5,6,7,8,9]}))

