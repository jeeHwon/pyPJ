import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
from Investar import Analyzer

mk = Analyzer.MarketDB()
naver = mk.get_daily_price('NAVER', '2019-01-02')
samsung = mk.get_daily_price('삼성전자', '2019-01-02')

df = pd.DataFrame({'X' : naver['close'], 'Y': samsung['close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}'

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['DOW x KOSPI', regr_line])
plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()