import pandas as pd 
import math
from datetime import datetime
import numpy as np
from pandas.core.series import Series

date = "2020-12-14"
df = pd.read_csv("C:/myData/STStatus/stat{}.csv".format(date), error_bad_lines=False)

df2 = pd.DataFrame({
    'DATE':df['DATE'],
    'CODE':df['CODE'],
    'NAME':df['NAME'],
    'OPEN':df['OPEN'],
    'HIGH':df['HIGH'],
    'LOW':df['LOW'],
    'CLOSE':df['CLOSE'],
    'BUY':df['BUY_UNIT'],
    'SELL':df['SELL_UNIT'],
    'QTY':df['QTY']
})
print(df2)
df2.to_csv("C:/myData/TodayStatus/stat{}.csv".format(date), index = False)