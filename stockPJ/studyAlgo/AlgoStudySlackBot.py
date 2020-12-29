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
# 김우철 chul(소프)
# 김한승 han    
# 백관호 baeck  
# 송진호 song   
# 이다희 Lee    
# 정    Jung    
# 최원석 choi   
# Karen karen   
# 지 Jee    

columns = ['WEEKS', 'STAGE', '_BAEK', '_CHOI','_CHUL','__HAN','__JEE','_JUNG','KAREN','_SONG']
rows = []
#            ['WEEKS', 'STAGE', '_BAEK', '_CHOI', '_CHUL', '__HAN', '__JEE', '_JUNG', 'KAREN', '_SONG']
rows.append(['____1', '____7', '_1157', '_____', '_2941', '_1110', '_1316', '_4344', '_1065', '_1152' ])
rows.append(['____2', '____8', '10250', '_____', '_2869', '_4673', '_1011', '_2775', '_1193', '_1712' ])
rows.append(['____3', '____9', '_1929', '_____', '_1978', '_1929', '_2581', '_2581', '_1978', '_1929' ])
rows.append(['____4', '___10', '_____', '_____', '_____', '10870', '10870', '_____', '_____', '_____' ])
rows.append(['____5', '___11', '_____', '_____', '_____', '_____', '_____', '_____', '_____', '_____' ])
df = pd.DataFrame(rows, columns=columns)
print(df)
file_name = 'studystats'
df_slack = df.to_csv('stockPJ/studyalgo/'+file_name + '.csv', encoding = 'euc-kr', index=False, sep='\t')

# 실제 봇으로 공지 할때만 활성화 시킬것
slack.files.upload('stockPJ/studyalgo/'+file_name + '.csv', channels='#stats')

