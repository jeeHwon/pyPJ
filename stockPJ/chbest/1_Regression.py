import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
from Investar import Analyzer

# ---------------Input area---------------
STOCK1 = '대한항공'
STOCK2 = '아시아나항공'
START_DATE = '2017-1-1'
END_DATE = ''
# ----------------------------------------

mk = Analyzer.MarketDB()
stk1 = mk.get_daily_price(STOCK1, START_DATE, END_DATE)
stk2 = mk.get_daily_price(STOCK2, START_DATE, END_DATE)

df = pd.DataFrame({'X' : stk1['close'], 'Y': stk2['close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}'

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['{} x {}'.format(STOCK1, STOCK2), regr_line])
plt.title(f'{STOCK1} x {STOCK2} (R = {regr.rvalue:.2f})')
plt.xlabel('{} Industrial Average'.format(STOCK1))
plt.ylabel('{}'.format(STOCK2))
plt.show()