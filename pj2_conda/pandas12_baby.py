from os import name
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pandas.core.reshape.merge import merge

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

# 파일을 읽어 tmp에 각 데이터 프레임을 저장
# tmp = []
# for year in range(1880, 2011):
#     filename = 'data/baby/yob{}.txt'.format(year)
#     d1 = pd.read_csv(filename, names=['name', 'sex', 'births'])
#     d1['year'] = year
#     tmp.append(d1)

# 리스트에 있는 데이트 프레임 concat
# data = pd.concat(tmp, ignore_index=True)
# print(data)

# 년도와 성별에 따른 출생아수
# s1 = data.groupby(['year', 'sex'])['births'].sum()
# print(s1)

# merge() : 2개의 데이터프레임 기준에 의해 연결
person = pd.read_csv('data/survey/survey_person.csv')
# print(person)
survey = pd.read_csv('data/survey/survey_survey.csv')
# print(survey)
ps = pd.merge(person, survey, left_on='ident', right_on='person')
# print(ps)

visited = pd.read_csv('data/survey/survey_visited.csv')
# print(visited)
psv = ps.merge(visited, left_on='taken', right_on='ident')
# print(psv)  # 한 컬럼 기준으로 merge 했을 때 다른 컬럼명 다르면 임의로 이름 부여
