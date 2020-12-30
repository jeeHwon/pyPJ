import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv('data/rtest.csv')

print('==================문제1==================')
print('각 열의 데이터타입:\n',data.dtypes)               
print('행의 수:',data.shape[0])              
print('열의 수:',data.shape[1])          

print('==================문제2==================')
def getRegident(x):
    if x ==1:
        return "서울"
    elif x ==2:
        return "인천"
    elif x ==3:
        return "대전"
    elif x ==4:
        return "대구"
    else:
        return "시군구"
data['resident2'] = data['resident'].apply(getRegident)
print(data)

print('==================문제3==================')
print('값의 갯수\n', data.count())
print('누락된 값의 갯수\n', data.shape[0]-data.count())
data = data[data['age'].notnull()]
print(data)

print('==================문제4==================')
s1 = data['age']
print('age의 최소값:', s1.min())
print('age의 최대값:', s1.max())
print('age의 평균값:', s1.mean())

print('==================문제5==================')
plt.boxplot(data[data['age']>0.0]['age'])
plt.title('Age box-plot')
plt.ylabel('나이')
plt.show()

print('==================문제6==================')
def getAge(x):
    if x <=30:
        return "청년층"
    elif x <=55:
        return "중년층"
    else:
        return "장년층"
data['age2'] = data['age'].apply(getAge)
print(data)

print('==================문제7==================')
def getGender(x):
    if x ==1:
        return "남자"
    else:
        return "여자"
data['gender2'] = data['gender'].apply(getGender)
print(data)

print('==================문제8==================')
print('남자의 빈도수',data[data['gender2']=='남자'].shape[0]/data.shape[0])
print('여자의 빈도수',data[data['gender2']=='여자'].shape[0]/data.shape[0])

print('==================문제9==================')
data['count'] = 1
g2 = data.groupby('gender2')['count'].sum()
plt.pie(g2, 
    labels=g2.index, 
    colors=['orange', 'green'],
    autopct='%.2f%%')
plt.title('남녀 빈도수 pie-chart')
plt.show()

print('==================문제10==================')
plt.scatter(data['age'],data['price'], c=data['gender'])
plt.title('나이에 따른 구매비용')
plt.xlabel('나이')
plt.ylabel('구매비용')
plt.show()