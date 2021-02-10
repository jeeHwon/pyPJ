from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np

# data = input_data.read_data_sets("../mnist/data/", one_hot=True)
# print(data.train)   # 학습용 데이터
# print(data.test)    # 검증용 데이터
# print('학습용데이터 갯수: ', data.train.num_examples)         # 55000
# print('검증용데이터 갯수: ', data.test.num_examples)          # 10000
# print('학습용데이터의 첫번째 데이터', data.train.labels[0:1])   # 7
# print('학습용데이터의 실제이미지', data.train.images[0:1])
# print('학습용데이터의 실제이미지', data.train.images[0:1].shape)
# plt.imshow(data.train.images[0:1].reshape(28,28), cmap='Greys', interpolation='nearest')
# plt.show()

# print('학습용데이터의 오만번째 데이터', data.train.labels[49999:1])
# plt.imshow(data.train.images[49999:50000].reshape(28,28), cmap='Greys', interpolation='nearest')
# plt.show()

# 과제)r에서 car데이터를 가져와 car.csv로 저장하고 세로로 읽어 출력,그래프로 그리시오
import pandas as pd
import seaborn as sns
from matplotlib import font_manager, rc

# 그래프처리 및 파일 로드
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# ver1.0
df = pd.read_csv('data/cars.csv')
df = df.loc[:,['speed','dist']]
df.to_csv('data/cars.csv', index=False)
data = np.loadtxt('data/cars.csv', skiprows=1, delimiter=',')
x = data[:, 0]
y = data[:, 1]
plt.figure(figsize=(20,10))
plt.title('자동차 속도에 따른 제동거리')
plt.xlabel('speed')
plt.ylabel('dist')
sns.lineplot(x=x, y=y)
plt.show()

# ver2.0
# data = np.loadtxt('data/cars.csv', delimiter=',', skiprows=1, unpack=True)
# print(data)
# plt.plot(data[0,:], data[1,:])
# plt.xlabel('speed')
# plt.ylabel('dist')
# plt.show()