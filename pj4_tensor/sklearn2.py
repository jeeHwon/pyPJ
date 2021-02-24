import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# colors=[['red','green','blue','orange'],
#     ['pink','ivory','purple','tomato']]
# data = pd.DataFrame(colors, columns=['a','b','c','d'])
# print(data)
# print("="*30)
# for d in data:
#     print(d) # 열이름
# print("="*30)
# for k, v in data.iteritems():
#     print('k=',k) # 열이름
#     print('v=\n',v) # 행인덱스, 값
# print("="*30)
# for k, v in data.iterrows():
#     print('k=',k) # 행인덱스
#     print('v=',v) # 열이름, 값
# print("="*30)
# for t in data.itertuples():
#     print('t=',t) # 튜플
#     print(t[0]) # 행인덱스
#     print(t[1]) # 0번째 열
#     print(t[2]) # 1번쨰 열
#     print(t[3]) # 2번째 열
#     print(t[4]) # 3번째 열
# print("="*30)
# =============================================================


# # 독버섯, 식용버섯 랜던포레스트 분류 학습
# mush= pd.read_csv('data/mushroom.csv', header=None)
# # print(mush)
# data = []
# label= []
# for k, v, in mush.iterrows():
#     # print('k=',k)
#     # print('v=\n',v)
#     label.append(v[0])
#     temp = []
#     for i in v.iloc[1:]:
#         temp.append(ord(i))
#     data.append(temp)
# # print(label) # 정답
# # print(data) # 데이터
# # 75% 학습, 25% 검증
# train_x, test_x, train_y, test_y = train_test_split(data, label, train_size=0.75)
# model = RandomForestClassifier()
# model.fit(train_x, train_y)
# pred = model.predict(test_x)
# print('정확도=',accuracy_score(pred, test_y))
# ================================================================

a = ['one','two','three','four','five','six']
k = 3
csvk = [[] for i in range(k)]
print(csvk) # [[], [], []]
for i in range(len(a)):
    csvk[i%k].append(a[i]) 
print(csvk) # [['one', 'four'], ['two', 'five'], ['three', 'six']]
for testdata in csvk:
    print('검증용data=',testdata)
    traindata = []
    for i in csvk:
        if i != testdata:
            traindata += i
    print('훈련용data=',traindata)




# iris 데이터 훈련용, 검증용 데이터 나눠 학습
# def split_x_y(data):
#     x = []
#     y = []
#     for d in data:
#         x.append(d[:4])
#         y.append(d[4])
#     return x, y

# data = open('data/iris.csv').read().split('\n')
# # print(data)
# del data[0]
# # print(data)
# csv = []
# for line in data:
#     temp= []
#     line = line.split(',')
#     # print(line)
#     temp.append(float(line[0]))
#     temp.append(float(line[1]))
#     temp.append(float(line[2]))
#     temp.append(float(line[3]))
#     temp.append(line[4])
#     # print(temp)
#     csv.append(temp)
# # print(csv)
# # 데이터 분할
# k = 5
# csvk = [[] for i in range(k)] # [[], [], [], [], []]
# # print(csvk)
# for i in range(len(csv)): # i=0, 1, 2, ...149
#     csvk[i%k].append(csv[i])
# # print(csvk)
# # print(len(csvk)) # 5 
# # print(len(csvk[0])) # 30
# scores= []
# for testdata in csvk:
#     print('검증용 data=', testdata) # 2차원
#     traindata = []
#     for i in csvk:
#         if i != testdata:
#             # traindata.append(i) # 3차원
#             traindata += i # 2차원
#     print('훈련용 data=', traindata) 
#     test_x, test_y = split_x_y(testdata)
#     print('test_x=',test_x)
#     print('test_y=',test_y)
#     train_x, train_y = split_x_y(traindata)
#     # 모델 생성
#     model = SVC()
#     model.fit(train_x, train_y)
#     pred = model.predict(test_x)
#     # print('정확도=',accuracy_score(pred,test_y))
#     scores.append(accuracy_score(pred,test_y))
# print('정확도', scores)
# print('전체정확도', sum(scores)/len(scores))

