# NLP : 인간의 언어를 머신에게 이해시키기 위한 분야
# 말의 의미는 단어로 구성 -> 머신에게 단어의 의미를 이해시키기
# 1) 시소러스(thesaurus) : 유의어 사전, 직접 단어의 의미를 정의, 
#   뜻이 같은 단어나 뜻이 비슷한 단어를 그룹으로 분류, 언어의 변동성에 적응 X
# 2) 통계기반
# 3) 추론기반

# National Language Toolkit
# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet
# print(wordnet.synsets('car'))
c1 = wordnet.synset('car.n.01')
# print('인간 - car:',c1.definition())
# print('동의어그룹에 속한 단어 - car:',c1.lemma_names())
# print('상위어 - car:',c1.hypernyms())
# print('상위어경로 - car:',c1.hypernym_paths())
# print('하위어 - car:',wordnet.synset('car.n.01').hyponyms())

# 단어간 유사도 구하기(0-1의 값)
# e1 = wordnet.synset('entity.n.01')
# b1 = wordnet.synset('book.n.01')
# d1 = wordnet.synset('dog.n.01')
# print('상위어경로',d1.hypernym_paths())
# print('책과 자동차의 유사도',b1.path_similarity(c1))
# print('책과 강아지의 유사도',b1.path_similarity(d1))
# cat = wordnet.synset('cat.n.01')
# print('고양이와 강아지의 유사도',cat.path_similarity(d1))
# print('고양이와 자동차의 유사도',cat.path_similarity(c1))
# tiger1 = wordnet.synset('tiger.n.1')
# tiger2 = wordnet.synset('tiger.n.2')
# # print(tiger1.definition())
# # print(tiger2.definition())
# print('고양이와 호랑이의 유사도',cat.path_similarity(tiger2))
# kitty = wordnet.synset('kitty.n.03')
# # print(kitty.definition())
# print('고양이와 키티의 유사도',cat.path_similarity(kitty))

# 정규화
import nltk
from nltk.corpus import stopwords
# nltk.download('punkt')
from nltk.tokenize import word_tokenize,sent_tokenize
# text = 'This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.'
# # 1)토큰화 : 문자열을 여러개의 조각으로 나눔. 문장토큰나이저, 단어토큰나이저
# words = word_tokenize(text)
# print('단어 :', words)
# # 2)단어의 대소문자 통일
# words = [w.lower() for w in words]
# print('소문자로 :',words)
# print('단어의 갯수 :',len(words))
# # 3)불용어 제거 : stopwords
# # nltk.download('stopwords')
# print('stopwords :',stopwords.words('english'))
# words = [w for w in words if w not in stopwords.words('english')]
# print('불용어 제거후 :',words)
# print('단어의 갯수 :',len(words))
# # 4)원형추출
# lem = nltk.WordNetLemmatizer()
# words = [lem.lemmatize(w) for w in words]
# print('원형추출후 :',words)
# # 5)품사태깅
# # nltk.download('averaged_perceptron_tagger')
# print(nltk.pos_tag(['pretty','girl']))

# alice에 적용
# text = open('data\\alice.txt').read()
# words = nltk.tokenize.word_tokenize(text)
# print('1)단어단위 자르기',len(words))
# words = [w.lower() for w in words]
# print('2)소문자로', words)
# words = [w for w in words if w not in stopwords.words('english') and w.isalnum()]
# print('3)불용어 제거후', len(words))
# print('불용어 제거후', words)
# lem = nltk.WordNetLemmatizer()
# words = [lem.lemmatize(w) for w in words]
# print('4)원형추출후 ', words)
# with open('data\\alice2.txt','w') as f:
#     f.write(' '.join(words))

# 가장 많이 나오는 단어 10개 추출
# from collections import Counter
# cnt = Counter(words)
# print(cnt.most_common(10))

# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# data = open('data\\alice2.txt').read()
# print(data)
# wc = WordCloud(background_color='white',max_words=2000).generate(data)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()

# 통계기반 기법=====================
# 말뭉치(대량의 텍스트 데이터)를 이용
# 1)말뭉치 전처리
import numpy as np
text = 'You say goodbye and I say hello.'
text = text.lower()   #소문자로
text = text.replace('.',' .')
words = text.split(' ') #단어단위 분할
print(words)
word2id={}
id2word={}
for w in words:
    if w not in word2id:
        position = len(word2id)
        word2id[w] = position
        id2word[position] = w
# print(word2id)
# print(id2word)
# print(word2id['say'])   #1
# print(id2word[5])   #hello
# 단어목록을 id목록으로 변환
corpus=[word2id[w] for w in words]
# print(corpus)
corpus=np.array(corpus)
# print(corpus)
def preprocess(text):
    text = text.lower()
    text = text.replace('.',' .')
    words = text.split(' ')
    word2id={}
    id2word={}
    for w in words:
        if w not in word2id:
            pos = len(word2id)
            word2id[w]=pos
            id2word[pos]=w
    corpus=np.array([word2id[w] for w in words])
    return corpus,word2id,id2word
text = 'You say goodbye and I say hello.'
print(text)
corpus,word2id,id2word=preprocess(text)
print('corpus=',corpus)
print('word2id=',word2id)
print('id2word=',id2word)

# 맥락:(주목하는 단어) 주변에 놓인 단어
# 통계기반기법: 어떤 단어에 주목했을때 그 주변에 어떤 단어가 몇번나오는지 세어서 집계
# ==윈도우 크기를 1로 한 경우
        # You say goodbye and I say hello  .
        # 0    1     2     3  4  1   5     6
# you :     0    1     0     0  0  0   0     0
# say :     1    0     1     0  1  0   1     0
# goodbye:  0    1     0     1  0  0   0     0

alice=open('data\\alice2.txt').read()
# print(alice)
corpus,word2id,id2word=preprocess(alice)
print('corpus=',corpus)
print('word2id=',word2id)
print('id2word=',id2word)