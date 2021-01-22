import seaborn as sns
# 과제 : tips데이터를 활용하여 성별 요일별 식대의 합을 출력하세요(피벗테이블 이용하세요)
tips = sns.load_dataset('tips')
tips_pivot = tips.pivot_table(index='day', columns='sex', values='total_bill' ,aggfunc='sum')
print(tips_pivot)