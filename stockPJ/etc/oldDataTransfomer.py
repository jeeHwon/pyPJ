from datetime import datetime
import numpy as np
from pandas.core.series import Series
import pandas as pd 

date = "2020-12-14"
df = pd.read_csv("C:/myData/STStatus/res{}.csv".format(date), error_bad_lines=False)
date = df['DATE']
code = df['CODE']
name = df['NAME']
open = df['OPEN']
high = df['HIGH']
low = df['LOW']
close = df['CLOSE']
buy = df['BUY']/df['QTY']
sell = df['SELL']/df['QTY']
qty = df['QTY']
df2 = pd.DataFrame()