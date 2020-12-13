import csv
symbol_list = ['A122630', 'A252670', 'A233740', 'A250780', 'A225130', 'A280940', 'A261220', 'A217770', 'A295000', 'A176950']
# csv 파일 읽기 
with open('C:/myApp/Investar/BB_TF_buylist.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f) 
    for i,line in enumerate(rdr): 
        if i==0: 
            symbol_list.extend(line)
print(symbol_list)