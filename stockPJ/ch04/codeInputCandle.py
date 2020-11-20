import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mplfinance as mpf 
from tqdm import tqdm
from tqdm import trange

# 종목코드 입력받기
ticker = input('종목코드 6자리 입력 : ')

# 맨뒤 페이지 숫자 구하기
url = 'https://finance.naver.com/item/sise_day.nhn?code={}&page=1'.format(ticker)
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

# 전체 페이지 읽어오기(tqdm으로 감싸서 progress bar 출력)
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code={}'.format(ticker)
for page in tqdm(range(1, int(last_page)+1)):
    page_url = '{}&page={}'.format(sise_url, page)
    df = df.append(pd.read_html(page_url, header=0)[0])

# 차트 출력 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:30]

df = df.rename(columns={'날짜':'Date', '시가':'Open', '고가':'High', '저가':'Low', '종가':'Close', '거래량':'Volume'})
df = df.sort_values(by='Date')
df.index = pd.to_datetime(df.Date) # error
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
# mpf.plot(df, title="Celltrion candle chart", type='candle')

kwargs = dict(title='{} customized chart'.format(ticker), type='candle', mav=(2,4,6), volume=True, ylabel='ohlc candle')
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df,**kwargs, style=s)
mpf.show()