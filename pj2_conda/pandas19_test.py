import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv('data/alcol.csv')

print('==================문제1==================')
data = data.set_index('State')
print('data 처음 5개\n',data.head())

print('==================문제2==================')
data_wine = pd.pivot_table(data, index = 'Year',  columns = 'State', values = 'Wine')
print(data_wine)

print('==================문제3==================')
data2009 = data[data['Year']==2009]
print('각 열의 데이터타입:\n',data2009.dtypes)               
print('행의 수:',data2009.shape[0])              
print('열의 수:',data2009.shape[1])  

print('==================문제4==================')
data2009 = data2009.drop('Year', axis=1)
data2009 = data2009.reset_index()  
print(data2009)

print('==================문제5==================')
print('값의 갯수\n', data2009.count())
print('누락된 값의 갯수\n', data2009.shape[0]-data2009.count())
data2009['Spirits'] = data2009['Spirits'].fillna(0)


print('==================문제6==================')
data2009['total'] = data2009['Beer'] + data2009['Wine'] + data2009['Spirits']
print(data2009)

print('==================문제7==================')
usa = pd.read_csv('data/usa.csv')
usa['country'] = '미국'
print(usa)

print('==================문제8==================')
df = pd.concat([data2009, usa], axis=1)
print(df)

print('==================문제9==================')
canada = pd.read_csv('data/canada.csv')
canada['country'] = '캐나다'
print(canada)

print('==================문제10==================')
pop = pd.concat([usa, canada])
pop = pop.set_index(['country', 'State'])
pop = pop.sort_index()
print(pop)