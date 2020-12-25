import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib
import numpy
# ===AZ_3DfToPl.py===
# df 파일을 읽어,
# 익절라인과 손절라인 별로 그래프를 그리고 최대수익률 내는 손절 및 익절 라인 계산하여, 
# 라인별 수익 그래프와 수치를 제공

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 마이너스 기호 처리
matplotlib.rcParams['axes.unicode_minus'] = False

# 익절라인 범위
xlist = numpy.arange(0.1, 25.0, 0.1)

df = pd.read_csv("df_BestLine.csv", error_bad_lines=False)
df = df.set_index('0.0')
print(df)
for i in range(df.shape[0]):
    plt.plot(xlist, df.iloc[i])
plt.title('라인에 따른 수익율 그래프')
plt.xlabel('익절라인')
plt.ylabel('수익률')

print('최대수익률:',df.max(axis=0).max())     # 최대 수익률
print('익절라인:',df.max(axis=0).idxmax())  # 최적 익절라인
print('손절라인:',df.max(axis=1).idxmax())  # 최적 손절라인
pd.set_option('display.max_row', 500)
print(df.loc[-19.9])

plt.show()