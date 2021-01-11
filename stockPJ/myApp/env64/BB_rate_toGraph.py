import pandas as pd 
import csv
import numpy
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)
plt.rcParams['axes.unicode_minus'] = False

path_dir = 'C:/myData/BB_rate_stat'
file_list = os.listdir(path_dir)
# print(file_list)
dftmp = []
for i in range(len(file_list)):
    df = pd.read_csv("C:/myData/BB_rate_stat/{}".format(file_list[i]))
    df['date'] = "{}".format(file_list[i][:-4])
    dftmp.append(df)


# 익절라인에 따른 수익률 그래프
# plt.style.use('ggplot')
# for i in range(len(dftmp)):
#     df = dftmp[i]
#     df = df.set_index('up_line')
#     df = df.sort_index()
#     plt.plot(df.index, df['suik'], label='{}'.format(df['date'][0.1]))

# plt.title('실현에 따른 수익률')
# plt.xlabel('파는시점')
# plt.ylabel('수익률')
# plt.legend(loc='best')
# plt.show()


dftmp = pd.concat(dftmp)
dftmp = dftmp.groupby('up_line')['suik'].mean()
print(dftmp.sort_values())
plt.plot(dftmp)
plt.style.use('ggplot')
plt.title('실현에 따른 수익률')
plt.xlabel('파는시점')
plt.ylabel('수익률')
plt.legend(loc='best')
plt.show()


