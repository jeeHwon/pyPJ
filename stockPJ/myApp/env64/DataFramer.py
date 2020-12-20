import pandas as pd 
import math
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
df = pd.read_csv("C:/myData/STResult/result{}.csv".format(date))
# print(df)

columns = ['DATE', 'CODE', 'NAME', 'BUY', 'SELL', 'QTY', 'FEE', 'OPEN','HIGH', 'LOW', 'CLOSE']
rows = []

# 처음 한줄 추가하고
rows.append([df.iloc[0]['DATE'], df.iloc[0]['CODE'], df.iloc[0]['NAME'], df.iloc[0]['BUY']* df.iloc[0]['QTY'], 
    df.iloc[0]['SELL']* df.iloc[0]['QTY'], df.iloc[0]['QTY'],(df.iloc[0]['BUY']* df.iloc[0]['QTY']+
    df.iloc[0]['SELL']* df.iloc[0]['QTY'])*0.00015, df.iloc[0]['OPEN'], df.iloc[0]['HIGH'],
    df.iloc[0]['LOW'], df.iloc[0]['CLOSE']])
for i in range(1, df.shape[0]): # df의 나머지 행에 접근
# for i in range(1, 10): # df의 나머지 행에 접근
    isIn = True
    for a in range(len(rows)):  # df의 한 행과 rows 모든 값중 같은 코드 있는지 확인
        if rows[a][1] == df.iloc[i]['CODE']:
            rows[a][3] = rows[a][3] + df.iloc[i]['BUY'] * df.iloc[i]['QTY']
            rows[a][4] = rows[a][4] + df.iloc[i]['SELL'] * df.iloc[i]['QTY']
            rows[a][5] = rows[a][5] + df.iloc[i]['QTY']
            rows[a][6] = rows[a][6] + df.iloc[i]['BUY'] * df.iloc[i]['QTY'] * 0.00015
            rows[a][6] = rows[a][6] + df.iloc[i]['SELL'] * df.iloc[i]['QTY'] * 0.00015
            rows[a][6] = rows[a][6] + df.iloc[i]['SELL'] * df.iloc[i]['QTY'] * 0.0025
            isIn = False
            break
    if isIn:
        rows.append([df.iloc[i]['DATE'], df.iloc[i]['CODE'], df.iloc[i]['NAME'], df.iloc[i]['BUY']* df.iloc[i]['QTY'],
            df.iloc[i]['SELL']* df.iloc[i]['QTY'], df.iloc[i]['QTY'],(df.iloc[i]['BUY']* df.iloc[i]['QTY']+
            df.iloc[i]['SELL']* df.iloc[i]['QTY'])*0.00015,df.iloc[i]['OPEN'],df.iloc[i]['HIGH'],
            df.iloc[i]['LOW'],df.iloc[i]['CLOSE']])


df2 = pd.DataFrame(rows, columns=columns)
# print(df2)
df2['QTY'] = df2['QTY']//2    # 자동입력시 활성회, 수동입력시 비활성화
tmp1 = []
tmp2 = []
tmp3 = []
for i in range(df2.shape[0]):
    tmp1.append(math.trunc(df2.iloc[i]['FEE']))
    tmp2.append(math.trunc(df2.iloc[i]['BUY']/df2.iloc[i]['QTY']))
    tmp3.append(math.trunc(df2.iloc[i]['SELL']/df2.iloc[i]['QTY']))
df2['FEE'] = tmp1
df2['RETURN'] = df2['SELL']-df2['BUY']-df2['FEE']
df2['BUY_UNIT'] = tmp2
df2['SELL_UNIT'] = tmp3

print(df2)
df2.to_csv("C:/myData/STStatus/stat{}.csv".format(date), index = False)



# rows = []
# rows.append(["a", "b", "c", 1, 2, 3])
# rows.append(["a", "b1", "c1", 4, 5, 6])
# rows.append(["a", "b11", "c11", 7, 8, 9])
# rows.append(["aa", "b11", "c11", 7, 8, 9])
# df = pd.DataFrame(rows, columns=columns)
# print(df)

# rows2 = []
# rows2.append([df.iloc[0]['DATE'], df.iloc[0]['CODE'], df.iloc[0]['NAME'], df.iloc[0]['BUY'], df.iloc[0]['SELL'], df.iloc[0]['QTY']])
# for i in range(1,df.shape[0]):    # 총 0 ,1, 2, 3 index로 접근
#     for a in range(len(rows2)):
#         if rows2[a][0] != df.iloc[i]['DATE']:
#             rows2.append([df.iloc[i]['DATE'], df.iloc[i]['CODE'], df.iloc[i]['NAME'], df.iloc[i]['BUY'], df.iloc[i]['SELL'], df.iloc[i]['QTY']])
#         else:
#             rows2[a][3] = rows2[a][3] + df.iloc[i]['BUY']

# df2 = pd.DataFrame(rows2, columns=columns)
# print(df2)