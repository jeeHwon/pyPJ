import matplotlib.pyplot as plt
import seaborn as sns

# 과제
# tips 데이터를 활용하여 흡연여부별 팁금액의 평균을 출력
tips = sns.load_dataset('tips')
tips = tips.groupby('smoker')['tip'].mean()
print(tips)
