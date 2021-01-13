import seaborn as sns

# 과제 tips를 읽어서 성별별 식대의 평균, 식대의 중간값, 팁의 합을 출력 agg이용
tips = sns.load_dataset('tips')
print(tips.groupby('sex').agg({'total_bill':['mean', 'median'], 'tip':'sum'}))
