import pandas as pd 

ebola = pd.read_csv('data/ebola.csv')
# ebola.info()


# melt() : 열의 데이터를 행으로
#   id_vars : 위치를 유지할 열 이름
#   var_name : 위치를 변경한 열의 데이터 이름
#   value_name : 위치를 변경한 열의 데이터 이름
ebola2 = ebola.iloc[:5, [0,2,3,10,11]]
# print(ebola2)
ebola3 = pd.melt(ebola2, id_vars='Date', var_name='kind', value_name='cnt' )
# print(ebola3)
# print(ebola3['new'].str.get(0))
# print(ebola3['new'].str.get(1))
# ebola4 = ebola.iloc[:5, [0,1,2,3,10,11]]
# print(ebola4)
# ebola5 = pd.melt(ebola4, id_vars=['Date', 'Day'])
# print(ebola5)
# print(ebola3['kind'][0].split('_')) # 하나씩 접근 비효율적이야.. 한꺼번에 접근할 수 있는방법?


# 데이터프레임 또는 시리즈에서 접근자
# 문자열 str / 날짜 dt
ebola3['new'] = ebola3['kind'].str.split('_')
ebola3['st'] = ebola3['new'].str.get(0)
ebola3['country'] = ebola3['new'].str.get(1)
ebola3 = ebola3.drop('new', axis=1)
# print(ebola3)
ebola3['st,country'] = ebola3['st']+ebola3['country']
# print(ebola3)
ebola3['Date'] = pd.to_datetime(ebola3['Date'])
ebola3['yy'] = ebola3['Date'].dt.year
ebola3['mm'] = ebola3['Date'].dt.month
ebola3['dd'] = ebola3['Date'].dt.day
print(ebola3)




