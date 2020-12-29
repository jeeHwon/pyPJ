import pandas as pd 

data = pd.read_csv('data/mov2.csv')
# print(data.head())
# data.info()

# ==과제
# 1) data 데이터프레임의 'Age'열을 활용하여 data['Newage'] 열을 생성
def getAge(x):
    if x ==1:
        return "Under 18"
    elif x ==18:
        return "18-24"
    elif x ==25:
        return "25-34"
    elif x ==35:
        return "35-44"
    elif x ==45:
        return "45-49"
    elif x ==50:
        return "50-55"
    else:
        return "56+"
data['Newage'] = data['Age'].apply(getAge)
print("===과제1 : data['Newage'] 열을 생성===")
print(data)

# 2) 연령대(['Newage'])별 평점점수의 평균 출력
g1 = data.groupby('Newage')['Rating'].mean()
print("===과제2 : 연령대별 평점점수의 평균 출력===")
print(g1)

# 3) 연령대별 평점점수가 낮은 사람 3건 출력
def getBottom3(x):
    print(x.sort_values(by='Rating', ascending=True)[:3])

g2 = data.groupby(['Newage','UserID'])['Rating'].mean()
g2 = g2.reset_index()
g2 = g2.groupby(['Newage'])
print("===과제3 : 연령대별 평점점수가 낮은 사람 3건 출력===")
g2.apply(getBottom3)