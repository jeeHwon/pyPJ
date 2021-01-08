import seaborn as sns
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

#과제
#1.팁의 히스토그램과 상자그림을 하나의 화면에 나타내세요
tips = sns.load_dataset('tips')

fig = plt.figure()
a1 = fig.add_subplot(2, 1, 1)
a2 = fig.add_subplot(2, 1, 2)
a1.hist(tips['tip'],bins=20, color='red')
a2.boxplot(tips['tip'])
plt.show()