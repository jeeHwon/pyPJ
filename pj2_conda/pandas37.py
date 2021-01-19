import matplotlib.pyplot as plt
import seaborn as sns

# 팁스데이터 이용해서 요일별식대의 합을 그래프로 출력
tips = sns.load_dataset('tips')
tips.info()
tips = tips.groupby('day')['total_bill'].sum()
tips = tips.reset_index()

sns.barplot(data=tips, x= "day", y= "total_bill")
plt.show()

