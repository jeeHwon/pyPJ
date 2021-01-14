import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

# 그래프처리 및 파일 로드
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)
report = pd.read_csv('data/report.csv')
bank = pd.read_csv('data/bank.csv')
tips = sns.load_dataset('tips')

print('==================문제1==================')
qustion1 = '''
데이터 시각화의 개념과 목적
1) 개념 : 데이터 시각화(Data Visualization)는 데이터를 분석하고 그 결과를 시각적으로 
        정보 전달 하는 모든 과정을 뜻한다. 특히 현대 환경의 변화와 빅데이터의 증가로 인하여
        이러한 데이터 시각화의 필요성이 더욱 증가 되었다.
2) 목적 : 그래프(graph)라는 수단으로 정보를 효과적이고 명확히 전달하는 것에 그 목적이 있다.
'''
print(qustion1)

print('==================문제2==================')
print(report.info())
print(report.head(10))
print(report.tail(10))

print('==================문제3==================')
report_new = report[report['State']=='New Hampshire']
plt.scatter(report_new['Beer'], report_new['Wine'])
plt.xlabel('맥주소비량')
plt.ylabel('와인소비량')
plt.title('맥주소비량과 와인소비량의 산점도')
plt.show()

print('==================문제4==================')
report_pivot = report.pivot('Year', 'State' , 'Beer')
stateList = ['New Hampshire', 'Colorado', 'Utah']
plt.style.use('ggplot')
for i in range(len(stateList)):
    plt.plot(report_pivot[stateList[i]])
plt.legend(stateList, loc='best')
plt.xlabel('년도')
plt.ylabel('맥주소비량')
plt.title('주별 맥주 소비량의 변화')
plt.show()

print('==================문제5==================')
print('각 열의 데이터타입:\n',tips.dtypes)               

print('==================문제6==================')
g1 = tips.groupby('time').agg({'total_bill':['min', 'max', 'mean', 'median']})
print(g1)
plt.boxplot([tips[tips['time']=='Lunch']['total_bill'],
            tips[tips['time']=='Dinner']['total_bill']], 
            labels=['Lunch','Dinner'])
plt.xlabel('time')
plt.ylabel('total_bill')
plt.title('식사시간별 식사비용의 box_plot')
plt.show()

print('==================문제7==================')
print(tips)
g1 = tips.groupby(['size','day']).agg({'total_bill':'sum'})
g1 = g1.reset_index()
tips_pivot = g1.pivot('size', 'day' , 'total_bill')
print(tips_pivot)

print('==================문제8==================')
dayList  = ['Thur', 'Fri', 'Sat', 'Sun']
g2 = tips.groupby(['size','day']).agg({'total_bill':'sum'})
g2 = g2.reset_index()
tips_pivot2 = g2.pivot('size', 'day' , 'total_bill')
plt.style.use('ggplot')
for i in range(len(dayList)):
    plt.plot(tips_pivot2[dayList[i]])
plt.legend(dayList, loc='best')
plt.xlabel('좌석수')
plt.ylabel('식사비용')
plt.title('식사 비용 현황')
plt.show()

print('==================문제9==================')
print(bank.info())
bank['Closing Date'] = pd.to_datetime(bank['Closing Date'])
bank['Updated Date'] = pd.to_datetime(bank['Updated Date'])
print(bank.info())

print('==================문제10==================')
bank['Closing Date'] = pd.to_datetime(bank['Closing Date'])
bank['year'] = bank['Closing Date'].dt.year
bank_year = bank.groupby('year').size()
plt.plot(bank_year)
plt.xticks(list(range(2000,2020,2)))
plt.title('연도별 파산한 은행수')
plt.show()