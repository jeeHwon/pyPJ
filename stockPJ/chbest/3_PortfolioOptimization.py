import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from Investar import Analyzer

# ---------------Input area---------------
STOCK1 = '삼성전자'
STOCK2 = 'SK하이닉스'
STOCK3 = '현대자동차'
STOCK4 = 'NAVER'
START_DATE = '2020-1-1'
END_DATE = ''
# ----------------------------------------

mk = Analyzer.MarketDB()
stocks = [STOCK1, STOCK2, STOCK3, STOCK4]
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, START_DATE, END_DATE)['close']

daily_ret = df.pct_change()
annual_ret = daily_ret.mean() * 252
daily_cov = daily_ret.cov()
annual_cov = daily_cov * 252

port_ret = []
port_risk = []
port_weights = []
sharpe_ratio = []

for _ in range(20000):
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)
    
    returns = np.dot(weights, annual_ret)
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    port_ret.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)
    sharpe_ratio.append(returns/risk)

portfolio = {'Returns':port_ret, 'Risk':port_risk, 'Sharpe':sharpe_ratio}
for i, s in enumerate(stocks):
    portfolio[s] = [weight[i] for weight in port_weights]
df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk', 'Sharpe'] + [s for s in stocks]]

max_sharpe = df.loc[df['Sharpe']==df['Sharpe'].max()]
min_risk = df.loc[df['Risk']==df['Risk'].min()]

df.plot.scatter(x='Risk', y='Returns', c='Sharpe', cmap='viridis', edgecolors='k', figsize=(11, 7), grid=True)
plt.scatter(x=max_sharpe['Risk'], y=max_sharpe['Returns'], c='r', marker='*', s=300)
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r', marker='X', s=200)
plt.title('Efficient Frontier')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
print("max_sharpe:\n",max_sharpe)
print("min_risk:\n",min_risk)
plt.show()