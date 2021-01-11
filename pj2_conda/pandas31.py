import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import font_manager, rc
from datetime import datetime

fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

#과제 bank.csv를 읽어 년도별 파산한 은행수를 선그래프로 스타일을 적용하여 이쁘게 작성하세요

bank = pd.read_csv('data/bank.csv', parse_dates=['Closing Date', 'Updated Date'])
bank.info()
bank['year'] = bank['Closing Date'].dt.year
s1 = bank.groupby('year').size()
plt.plot(s1)
plt.xticks(list(range(2000,2020,2)))
plt.title('연도별 파산한 은행수')
plt.show()