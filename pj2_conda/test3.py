# 빅데이터 분석 결과 시각화
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

# 그래프처리 및 파일 로드
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv('data/report.csv')
# 1)
# 2)
# 3)
# data.info()
# print(data.head(10))
# print(data.tail(10))
# plt.scatter(data[data['State']=='New Hampshire']['Beer'], data[data['State']=='New Hampshire']['Wine'])
# plt.show()

# 4)
# plt.style.use('ggplot')
# plt.plot(data[data['State']=='New Hampshire']['Year'], data[data['State']=='New Hampshire']['Wine'])
# plt.plot(data[data['State']=='Utah']['Year'], data[data['State']=='Utah']['Wine'])
# plt.legend(['New Hampshire', 'Utah'])
# plt.title('주별 맥주 소비량의 변화')
# plt.xlabel('년도')
# plt.ylabel('맥주소비량')
# plt.show()

# 5)
tips = sns.load_dataset('tips')
print(tips.dtypes)

# 6)
# print(tips['total_bill'].min())
# print(tips['total_bill'].max())
# print(tips['total_bill'].mean())
# print(tips['total_bill'].median())
# plt.boxplot(tips['total_bill'])
# plt.show()

# 7)
# p1 = pd.pivot_table(tips, index='size', columns='day',values='total_bill', aggfunc='sum')
# print(p1)

# 8)
# plt.plot(p1.index, p1)
# plt.legend(p1.columns)
# plt.xlabel('좌석수')
# plt.ylabel('식사비용')
# plt.title('식사비용현황')
# plt.show()

# 9)
bank = pd.read_csv('data/bank.csv', parse_dates=['Closing Date', 'Updated Date'])
bank.info()

# 10)
bank['yy'] = bank['Closing Date'].dt.year
print(bank.head())
s1 = bank.groupby('yy').size()
print(s1)
plt.plot(s1)
plt.show()