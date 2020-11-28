import pandas as pd 
import mplfinance as mpf 
import matplotlib.pyplot as plt 
from Investar import Analyzer

# ---------------Input area---------------
STOCK = '현대자동차'
START_DATE = '2019-1-1'
END_DATE = ''
MA1 = 5
MA2 = 20
MA3 = 120
# ----------------------------------------

mk = Analyzer.MarketDB()
df = mk.get_daily_price(STOCK, START_DATE, END_DATE)
df = df[['date', 'close', 'diff', 'open', 'high', 'low', 'volume']]

df.index = pd.to_datetime(df.date)
df = df[['open', 'high', 'low', 'close', 'volume']]

kwargs = dict(title='{} customized chart'.format(STOCK), type='candle', mav=(MA1,MA2,MA3), volume=True, ylabel='ohlc candle')
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df,**kwargs, style=s)
mpf.show()