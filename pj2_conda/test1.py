import pandas as pd
# 분석용 데이터 구축
# 1)
data = pd.read_csv('data/alcol.csv')
data = data.set_index('State')
print(data.head())

# 2) 
data_wine = pd.pivot_table(data, index='Year', columns='State', 
    values='Wine', aggfunc=sum)
print(data_wine)

# 3)
data2009 = data[data['Year']==2009]
print(data2009.shape)

# 4)
data2009 = data2009.drop('Year', axis=1)
data2009 = data2009.reset_index()
print(data2009.head())

# 5)
print('누락값의 수\n',data2009.shape[0]-data2009.count())
data2009 = data2009.fillna(0)

# 6)
data2009['total'] = data2009['Beer']+data2009['Wine']+data2009['Spirits']
print(data2009.head())

# 7)
usa = pd.read_csv('data/usa.csv')
usa['country'] = '미국'
print(usa.head())

# 8)
df = pd.merge(data2009, usa, on='State')
df= df.set_index('State')
print(df.head())

# 9)
canada = pd.read_csv('data/canada.csv')
canada['country'] = '캐나다'
print(canada.head())

# 10)
pop = pd.concat([usa,canada], ignore_index=True)
pop = pop.set_index(['country','State'])
print(pop.head())

