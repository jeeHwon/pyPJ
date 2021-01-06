import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_excel('data\\시도별 전출입 인구수.xlsx')
# print(data.head(10))
data = data.fillna(method='ffill')
# print(data.head(10))

# 서울에서 다른 지방으로 이사한 데이터만 그래프로
d1 = data[(data['전출지별']=='서울특별시') & (data['전입지별']!='서울특별시')]
d1 = d1.drop('전출지별', axis=1)
d1 = d1.rename(columns={'전입지별':'전입지'})
d1 = d1.set_index('전입지')
# print(d1)

dk = d1.loc['경기도']
dp = d1.loc['부산광역시']
dg = d1.loc['광주광역시'] # '-' 데이터 포함되어 있어 전처리  필요
d2 = d1.loc[['부산광역시','광주광역시','제주특별자치도']]  
# 방법 1) numpy 이용
dg = np.where(dg.values=='-', 0, dg.values)
# 방법 2) to_nueric 이용
d2 = d2.transpose()     # 행열전환
d2['광주광역시'] = pd.to_numeric(d2['광주광역시'], errors='coerce')
d2['광주광역시'] = d2['광주광역시'].fillna(0)

# # 사용가능한 style
# print('스타일 종류\n', plt.style.available)
# # 사용가능한 colors
# colors = {}
# for n,h in matplotlib.colors.cnames.items():
#     colors[n] = h
# print('색상종류\n',colors)
# plt.plot(dk)            # 선그래프
# plt.plot(dk, 'o')       # 점그래프
# plt.plot(dk, marker='o', markerfacecolor='green', color='red', linewidth=2)
# plt.plot(dk, marker='+', markerfacecolor='green', color='red', linewidth=2)
# plt.plot(dk, marker='*', markerfacecolor='green', color='red', linewidth=2)
# plt.plot(dk, marker='.', markerfacecolor='green', color='red', linewidth=2)


plt.style.use('dark_background')         # 스타일지정
plt.figure(figsize=(20,8))
plt.plot(dk)                     # 서울->경기
plt.plot(dp)                     # 서울->부산
plt.plot(d1.loc['제주특별자치도']) # 서울->제주
plt.plot(dg)                     # 서울->광주

plt.title('서울 -> 타지역 전입 현황', size=20)
plt.xlabel('연도')
plt.ylabel('이동수')
plt.xticks(size=10, rotation=70)
plt.yticks(size=10)
plt.legend(['서울->경기','서울->부산','서울->제주','서울->광주'], fontsize=10)
plt.annotate('인구이동 증가', xy=(10,400000), fontsize=10, ha='center', rotation=30)
plt.annotate('인구이동 감소', xy=(35,500000), fontsize=10, ha='center', rotation=-30)
# plt.annotate('', xy=(), xytext=(), ....) # xytext=(화살표꼬리부분), xy=(화살표머리부분) 
plt.annotate('', xytext=(4,300000), xy=(19,550000),  arrowprops=dict(arrowstyle='->', color='red', lw=3)) 
plt.annotate('', xytext=(30,580000), xy=(43,380000),  arrowprops=dict(arrowstyle='->', color='blue', lw=3)) 
plt.show()

