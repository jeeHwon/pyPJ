import pandas as pd 
from numpy import NaN, nan, NAN
df = pd.read_csv('C:/myData/AZ_test.csv')
df.info()
df = df.sort_values(by="ROI", ascending=False)
# df = df[df['UNDER']==-20.0]
print(df.head(10))
# print(df[df['OVER']==14.9])


