import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# tips 데이터를 데이터프레임으로 읽고 식대와 팁과의 관계를 그래프로 표현(산점도) 투명도 alpha 값을 0.5로
tips = sns.load_dataset('tips')

plt.scatter(tips['total_bill'],tips['tip'], alpha=0.5) 
plt.title('식대-팁 산점도')
plt.xlabel('식대')
plt.ylabel('팁')
plt.show()
