import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_excel('data\\시도별 전출입 인구수.xlsx')
data = data.fillna(method='ffill')

# 과제 서울에서 경기, 부산, 광주, 제주로 이사한 데이터를 각각 선그래프로
d1 = data[(data['전출지별']=='서울특별시') & (data['전입지별']!='서울특별시')]
d1 = d1.drop('전출지별', axis=1)
d1 = d1.rename(columns={'전입지별':'전입지'})
d1 = d1.set_index('전입지')
dk = d1.loc['경기도']
dp = d1.loc['부산광역시']
dj = d1.loc['제주특별자치도']
d2 = d1.loc[['부산광역시','광주광역시','제주특별자치도']]
d2 = d2.transpose()   
d2['광주광역시'] = pd.to_numeric(d2['광주광역시'], errors='coerce')
dg = d2['광주광역시'].fillna(0)

plt.style.use('ggplot')

fig, axs = plt.subplots(ncols=2, nrows=2)
ax1, ax2, ax3, ax4 = axs.ravel()

x = np.arange(1970, 2018, 1)
ax1.plot(x,dk)
ax2.plot(x,dp)  
ax3.plot(x,dg)  
ax4.plot(x,dj) 

ax1.set_title('서울->경기')
ax2.set_title('서울->부산')
ax3.set_title('서울->광주')
ax4.set_title('서울->제주')

fig.suptitle('서울 -> 타지역 전입 현황', size=20)
plt.show()