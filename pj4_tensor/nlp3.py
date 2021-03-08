# pip install gensim
import re
from gensim.models.word2vec import Word2Vec,Text8Corpus

# Word2vec 활용 - 영문
# data = open('data\grim.txt', encoding='utf-8').read()
# print(data)
# text = data[2674:53000]
# text = re.sub(r'[^a-zA-Z\.]',' ',text)
# print(text)
# sen = text.split('.') # 문장단위로 자르기
# print(sen)
# words = [s.split(' ') for s in sen]
# print(words)
# print(words0])
# model = Word2Vec(words, sg=1, size=100, window=3, min_count=3)
# sg 알고리즘 선택  0:CBOW, 1:skip gram
# size 벡터크기
# window 단어로부터 거리
# min_count 사용할 단어의 최소빈도
# model.save('data/grim.model')

# model = Word2Vec.load('data/grim.model')
# print('princess 단어를 벡터로', model.wv['princess'])
# print('princess 단어를 벡터로', model.wv['princess'].shape)
# print('유사도', model.similarity('princess','queen'))
# print('가장 유사한 단어', model.most_similar('princess'))
# print('가장 유사한 단어 3개 추출', model.most_similar('princess', topn=3))
# print('가장 유사한 단어',model.most_similar(positive=['princess','man'], negative=['woman']))


# Word2Vec 활용 - 국문
from konlpy.tag import Okt
with open('data/news.csv', encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
okt = Okt()
result = []
for line in lines:
    mallist = okt.pos(line, norm=True, stem=True)
    temp = []
    for word in mallist:
        if not word[1] in ['Alpha','Punctuation','Josa','Number','Emoi','Foreign']:
            temp.append(word[0])
    # print(temp)
    result.append(' '.join(temp))
# print(result)
data = ' '.join(result)