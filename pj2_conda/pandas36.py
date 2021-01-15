import seaborn as sns
# 과제 : tips 데이터를 이용하여 요일을 행인덱스, 성별을 열인덱스로 하여 식사금액의 합을 출력
tips = sns.load_dataset('tips')
tips_pivot = tips.pivot_table(index='day', columns='sex', values='total_bill' ,aggfunc='sum')
print(tips_pivot)