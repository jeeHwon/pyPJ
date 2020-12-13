from pandas.core.frame import DataFrame
from slacker import Slacker
import os
import pandas as pd
def getPwd():
    with open ('C:\\myKey\\studybot.txt') as f:
        pw = f.readline()
    return pw.strip()
slack = Slacker(getPwd())
# NAMING
# 김우철 chul
# 김한승 han    
# 백관호 baeck  
# 송진호 song   
# 이다희 Lee    
# 정    Jung    
# 최원석 choi   
# Karen karen   
# 지 Jee    

name = ['chul', 'han', 'baek','song','lee','jung','choi','karen','jee']


columns = ['WEEKS', 'STAGE', '_BAEK', '_CHOI','_CHUL','__HAN','__JEE','_JUNG','KAREN','__LEE','_SONG']
rows = []
#            ['WEEKS', 'STAGE', '_BAEK', '_CHOI', '_CHUL', '__HAN', '__JEE', '_JUNG', 'KAREN', '__LEE', '_SONG']
rows.append(['____1', '____7', '_1157', '_____', '_2941', '_1110', '_1316', '_4344', '_1065', '_____', '_1152' ])
rows.append(['____2', '____8', '10250', '_____', '_____', '_4673', '_1011', '_2775', '_1193', '_____', '_1712' ])
df = pd.DataFrame(rows, columns=columns)
print(df)
file_name = 'studystats'
df_slack = df.to_csv('studyAlgo/' + file_name + '.csv', encoding = 'euc-kr', index=False, sep='\t')

# 실제 봇으로 공지 할때만 활성화 시킬것
# slack.files.upload('studyAlgo/' + file_name + '.csv', channels='#stats')

