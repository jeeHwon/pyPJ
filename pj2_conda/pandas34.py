import pandas as pd 
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 과제 나라별 gap.tsv를 읽어 아프리카 대륙의 나라별 기대수명을 선그래프로

gaps = pd.read_csv(os.path.join('data', 'gap.tsv'), sep='\t')
print(gaps)

df = gaps[gaps['continent']=='Africa']
df = df.drop('continent', axis=1)
# print(df.index)
# countryList  = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi',
#                 'Cameroon', 'Central African Republic', 'Chad', 'Comoros',
#                 'Congo, Dem. Rep.', 'Congo, Rep.', "Cote d'Ivoire", 'Djibouti', 'Egypt',
#                 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana',
#                 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
#                 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco',
#                 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Reunion', 'Rwanda',
#                 'Sao Tome and Principe', 'Senegal', 'Sierra Leone', 'Somalia',
#                 'South Africa', 'Sudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia',
#                 'Uganda', 'Zambia', 'Zimbabwe']
# plt.style.use('ggplot')
# for i in range(len(countryList)):
#     plt.plot(df[df['country']==countryList[i]]['year'], df[df['country']==countryList[i]]['lifeExp'])
# plt.legend(countryList, loc='best')
# plt.xlabel('연도')
# plt.ylabel('기대수명')
# plt.title('아프리카 대륙의 전체 나라별 기대수명')
# plt.show()

# 3개국
# countryList  = ['Algeria', 'Angola', 'Benin']
# plt.style.use('ggplot')
# for i in range(len(countryList)):
#     plt.plot(df[df['country']==countryList[i]]['year'], df[df['country']==countryList[i]]['lifeExp'])
# plt.legend(countryList, loc='best')
# plt.xlabel('연도')
# plt.ylabel('기대수명')
# plt.title('아프리카 대륙의 3개국 나라별 기대수명')
# plt.show()

# 피벗이용
# p1 = df.pivot('year','country','lifeExp')
# countryList  = ['Algeria', 'Angola', 'Benin']
# plt.style.use('ggplot')
# for i in range(len(countryList)):
#     plt.plot(p1[countryList[i]])
# plt.legend(countryList, loc='best')
# plt.xlabel('연도')
# plt.ylabel('기대수명')
# plt.title('아프리카 대륙의 3개국 나라별 기대수명')
# plt.show()

g1=gaps[gaps['continent']=='Africa']
print(g1)
# 2) 1번의 데이터를 활용하여 3개국의 기대수명을 선그래프로
g2=g1.groupby('country')['lifeExp'].mean() # 아프리카대륙 각 나라의 평균기대수명
print(g2)
plt.hist(g2)
plt.show()