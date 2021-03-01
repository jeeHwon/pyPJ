from sklearn import linear_model
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import glob
import os

# # 사이킷런 
# train_x = [[0,0],[0,1],[1,0],[1,1]]
# train_y = [0,0,0,1]
# # 모델 생성
# model = LinearSVC()
# # 학습
# model.fit(train_x, train_y)
# # 예측
# test_x = [[0,0],[0,1],[1,0],[1,1]]
# pred = model.predict(test_x)
# # 평가
# print('정확도=', accuracy_score([0,0,0,1], pred))
# # =====================================================


# iris data
# 데이터와 정답으로 분리
# data = pd.read_csv('data/iris.csv')
# # print(data)
# x = data.loc[:, ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']]
# y = data.loc[:, 'Species']
# print(y)
# # print(x)
# # 70% 데이터로 훈련, 30% 데이터로 검증
# train_x, test_x, train_y, test_y = train_test_split(x, y, train_size=0.7, shuffle=True)
# # 모델 생성
# model = SVC()
# # 훈련 
# model.fit(train_x, train_y)
# # 평가
# pred = model.predict(test_x)
# print('정확도=', accuracy_score(test_y, pred))


# 그래프 그리기
# x = np.random.rand(100,1) # 0~1 사이의 숫자 100개
# print(x)
# x = x * 4 - 2
# print(x) # -2 <= x <= 2
# y = 3 * x - 2 + np.random.randn(100,1)
# plt.plot(x,y,'o')
# plt.show()
# # 모델생성
# model = LinearRegression()
# # 훈련
# model.fit(x,y)
# print('기울기=', model.coef_)
# print('절편=', model.intercept_)
# # 예측
# pred = model.predict(x)
# plt.plot(x,y,'o')
# plt.plot(x,pred)
# plt.show()
# =======================================================

# cars data
# data = pd.read_csv('data/cars.csv')
# print(data)
# print(list(data['speed']))
# x = []
# y = []
# for i in range(data.shape[0]):
#     # print(list(data['speed'])[i])
#     x.append([list(data['speed'])[i]])
#     y.append([list(data['dist'])[i]])
# print(x)
# print(y)
# model = linear_model.LinearRegression()
# # 훈련
# model.fit(x,y)
# print('기울기=', model.coef_)
# print('절편=', model.intercept_)
# # 예측
# pred = model.predict(x)
# plt.plot(x,y,'o')
# plt.plot(x,pred)
# plt.show()
# # ==============================================

# lang data
# print(ord('a')) # 97
# print(ord('A')) # 65
# print(chr(65)) # A
# print(sum([1,2,3,4,5]))
# a = [1,2,3,4,5]
# total = sum(a)
# print(total)
# # map(함수, 반복가능객체)
# print(map(lambda i: i/total, a))
# print(list(map(lambda i: i/total, a)))

# def make_data(file):
#     with open(file, encoding='utf-8') as f:
#         text = f.read()
#         text = text.lower()
#         # print(text)
#         cnt = [0 for i in range(26)]
#         # print(cnt)
#         for c in text:
#             n = ord(c)
#             if ord('a') <=  n <= ord('z'):
#                 cnt[n-ord('a')] += 1
#         # print(cnt)
#         total = sum(cnt)
#         data = list(map(lambda i:i/total, cnt))
#         # print(data)
#         return data

# def load_files(path):
#     # print(glob.glob(path))
#     label = []
#     data = []
#     file_list = glob.glob(path)
#     for file in file_list:
#         # print(os.path.dirname(file)) # 전체경로에서 마지막 제외한 주소
#         # print(os.path.basename(file)) # 전체경로에서 마지막 주소
#         # print(os.path.basename(file)[:2]) # 파일명 슬라이싱
#         d = make_data(file)
#         label.append(os.path.basename(file)[:2]) # 정답 추출
#         data.append(d)
#     # print(label)
#     # print(data)
#     return data, label
# train_x, train_y = load_files('data/lang/train/*.txt')
# test_x, test_y = load_files('data/lang/test/*.txt')
# # print(train_x)
# # print(train_y)
# model = SVC()
# model.fit(train_x, train_y)
# pred = model.predict(test_x)
# print('정확도=', accuracy_score(test_y, pred))
# ==================================================================

data = pd.read_csv('data/water.csv')
x = []
y = []
old = list(data['old'])
new = list(data['new'])
astime = list(data['as_time'])
for i in range(data.shape[0]):
    x.append([old[i], new[i]])
    y.append([astime[i]])
# print(x)
# print(y)
model = LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)
print('예측as 시간:', model.predict([[7000, 23000]]))
