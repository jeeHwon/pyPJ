import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# tensor6.py 복습
# data = np.loadtxt('data/zoo/zoo.csv',delimiter=',')
# print(data)
# ydata = data[:10, -1:]
# print(ydata)
# y = tf.placeholder(tf.int64,[None,1])
# onehot1 = tf.one_hot(y,7)
# onehot2 = tf.reshape(onehot1,[-1,7])
# argmax1 = tf.argmax(onehot2,1)
# argmax2 = tf.reshape(argmax1,[-1,1])
# equal1 = tf.equal(y,argmax2)
# cast1 = tf.cast(equal1,tf.float32)
# mean1 = tf.reduce_mean(cast1)
# sess = tf.Session()
# print('y=',sess.run(y,feed_dict={y:ydata}))
# print('onehot1=',sess.run(onehot1,feed_dict={y:ydata}))
# print('onehot2=',sess.run(onehot2,feed_dict={y:ydata}))
# print('argmax1=',sess.run(argmax1,feed_dict={y:ydata}))
# print('argmax2=',sess.run(argmax2,feed_dict={y:ydata}))
# print('equal1=',sess.run(equal1,feed_dict={y:ydata}))
# print('cast1=',sess.run(cast1,feed_dict={y:ydata}))
# print('mean1=',sess.run(mean1,feed_dict={y:ydata}))
# sess.close()


# 연속값 이산속성으로 변경하기
# a = np.array([[1,2,3],[4,5,6],[7,8,5]])
# print(a)
# print(a[:,-1])
# # 5미만 -> 0
# # 5이상 8이하 -> 9
# print(a[a[:,-1]<5])
# a[a[:,-1]<5,-1] = 0
# print(a)
# a[(a[:,-1]>=5)&(a[:,-1]<=8) ,-1] = 9
# print(a)

# 와인의 품질 <=4 -> 0 / <4<=7 -> 1 / <7 -> 2
# data = np.loadtxt('data/wine.csv',delimiter=';',skiprows=1)
# print(data)
# data[data[:,-1]<=4,-1] = 0
# data[(data[:,-1]>4)&(data[:,-1]<=7), -1] = 1
# data[data[:,-1]>7,-1] = 2
# print(data)
# print(data[:,-1])
# np.savetxt('data/wine2.csv',data)

# 그래프 이미지 저장
# data = pd.read_csv('data/wine2.csv', sep=' ', header=None)
# print(data)
# s1 = data.groupby(11).size()
# print(s1)
# plt.plot(s1)
# plt.show()
# plt.savefig('data/wine.png')  # 이미지 저장시

# 와인 데이터 학습하기
# data = np.loadtxt('data/wine2.csv')
# print(data.shape) # (4898, 12)
# np.random.shuffle(data)
# train_x, train_y = data[:3429,:11], data[:3429,11:]
# test_x, test_y = data[3429:,:11], data[3429:,11:]
# print(test_y)
# x = tf.placeholder(tf.float32,[None,11])
# y = tf.placeholder(tf.int32,[None,1])
# onehot = tf.one_hot(y,3) # 3차원
# onehot2 = tf.reshape(onehot,[-1,3])
# w = tf.Variable(tf.random_normal([11,3]))
# b = tf.Variable(tf.random_normal([3]))
# logits = tf.matmul(x,w)+b
# h = tf.nn.softmax(logits)
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=onehot2))
# train = tf.train.GradientDescentOptimizer(0.001).minimize(cost)
# corr = tf.equal(tf.argmax(h,1), tf.argmax(onehot2,1))
# acc = tf.reduce_mean(tf.cast(corr,tf.float32))

# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         sess.run(train,feed_dict={x:train_x, y:train_y})
#         if i %100 == 0:
#             print(sess.run(cost, feed_dict={x:train_x, y:train_y}))
#     print('정확도=',sess.run(acc,feed_dict={x:test_x, y:test_y}))
# ======================================================================

# 기상데이터
# data.kma.go.kr
# data = pd.read_csv('data/temp.csv', encoding='cp949', parse_dates=['일시'])
# data.info()
# print(data)
# data['yy'] = data['일시'].dt.year
# data['mm'] = data['일시'].dt.month
# data['dd'] = data['일시'].dt.day
# data = data.drop(['일시'], axis=1)
# data.columns = ['temp','yy','mm','dd']
# print(data)
# data = data.sort_values(['yy','mm','dd'])
# data.to_csv('data/temp2.csv', index=False)

# 일별 평균 기온
# data = pd.read_csv('data/temp2.csv')
# print(data)
# s1 = data.groupby(['mm','dd'])['temp'].mean()
# print(s1)
# plt.plot(s1.values)
# plt.show()

# 연도별 기온 -10 이하인 날
# cool = data[data['temp']<=-10]
# print(cool)
# s2 = cool.groupby('yy').size()
# print(s2)


# 3개의 데이터를 읽어 4번째 데이터를 예측
# a = [0,1,2,3,4,5]
# interval = 3
# x = []
# y = []
# for i in range(len(a)):
#     if i < interval:
#         continue
#     tempx = []
#     for j in range(interval): # i=3 0,1,2
#         z = i - interval + j
#         tempx.append(a[z])
#     x.append(tempx)
#     y.append(a[i])
# print('x=',x)
# print('y=',y)

# 6일치 온도데이터를 읽어 7일째의 기온 예측
def makedata(temp):
    interval = 6
    xdata = []
    ydata = []
    for i in range(len(temp)):
        if i < interval:
            continue
        ydata.append(temp[i])
        tempx = []
        for j in range(interval):
            z = i - interval + j
            tempx.append(temp[z])
        xdata.append(tempx)
    return xdata, ydata

data = np.loadtxt('data/temp2.csv', delimiter=',', skiprows=1)
print(data.shape) # (3653, 4)
train = data[data[:,1]<=2017, :]
test = data[data[:,1]>2017, :]
print(train.shape) # (2557, 4)
print(test.shape) # (1096, 4)

train_x, train_y = makedata(train[:,0])
test_x, test_y = makedata(test[:,0])
# print(train_y) # 1차원 리스트
train_y = np.array(train_y).reshape(-1,1)
test_y = np.array(test_y).reshape(-1,1)
# print(train_y) # 2차원 넘파이 배열

x = tf.placeholder(tf.float32, [None, 6])
y = tf.placeholder(tf.float32,[None,1] )
w = tf.Variable(tf.random_normal([6,1]))
b = tf.Variable(tf.random_normal([1]))
h = tf.matmul(x,w)+b
cost = tf.reduce_mean(tf.square(h-y))
train = tf.train.GradientDescentOptimizer(0.0003).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5001):
        sess.run(train, feed_dict={x:train_x, y:train_y})
        if i % 100 == 0:
            print(sess.run(cost, feed_dict={x:train_x, y:train_y}))
    result = sess.run(h,feed_dict={x:test_x})
plt.plot(test_y)
plt.plot(result)
plt.show()