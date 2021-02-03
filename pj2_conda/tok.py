import re
import pandas as pd 
from konlpy.tag import Hannanum

f = open("C:/Users/HOME/Desktop/tok.txt","r",encoding='UTF8')
text = f.read()

text = re.sub('[0-9]+', '', text)
text = re.sub('[A-Za-z]+', '', text)
text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ·!』\\‘’|\(\)\[\]\<\>`\'…》]', '', text)

hannanum = Hannanum()
text_list = hannanum.nouns(text)
for item in text_list:
    if item == '오후':
        text_list.remove('오후')
    if item == '오전':
        text_list.remove('오전')

word_list = pd.Series(text_list)
result = word_list.value_counts()
print(result)
result.to_csv("tok.csv")