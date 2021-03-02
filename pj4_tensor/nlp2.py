import numpy as np

# 통계기반 기법: 어떤 단어에 주목했을 때 그 주변에 어떤단어가 몇번 나오는지 세어 집계하는 방법
# 단어의 의미는 주변 단어에 의해 형성 -> 단어자체는 의미 없고 그 단어가 사용된 맥락이 의미를 형성
# text = 'You say goodbye and I say hello.'
# text = text.lower()
# text = text.replace('.', ' .')
# words = text.split(' ')
# print(words)
# word2id = {} #{you:0, say:1, ...}
# id2word = {} #{0:you, 1:say, ...}
# for word in words:
#     if word not in word2id:
#         pos = len(word2id)
#         word2id[word] = pos
#         id2word[pos] = word
# print(word2id)
# print(id2word)
# print(word2id['say'])
# print(id2word[3])
# corpus = [word2id[w] for w in words]
# print(corpus)
# corpus = np.array(corpus)
# print(corpus)

# 위 작업을 함수 형태로
def preprocess(text):
    text = text.lower()
    text = text.replace('.', ' .')
    words = text.split(' ')
    word2id = {} 
    id2word = {}
    for word in words:
        if word not in word2id:
            pos = len(word2id)
            word2id[word] = pos
            id2word[pos] = word
    corpus = np.array([word2id[w] for w in words])
    return corpus, word2id, id2word
text = 'You say goodbye and I say hello.'
corpus, word2id, id2word = preprocess(text)
# print(corpus)
# print(word2id)
# print(id2word)
textlist = ['king is a strong man',
        'queen is a wise woman',
        'boy is a young man',
        'girl is a young woman',
        'prince is a young king',
        'princess is a young queen',
        'man is strong',
        'woman is pretty',
        'prince is a boy will be king',
        'princess is a girl will be queen']
stop_words = ['is','a','will','be']
def delstopword(textlist):
    result = []
    for text in textlist:
        temp = text.split(' ')
        for stop_word in stop_words:
            if stop_word in temp:
                temp.remove(stop_word)
        result.append(' '.join(temp))
    return result
textlist = delstopword(textlist)
# print('textlist=', textlist)
# corpus, word2id, id2word = preprocess(' '.join(textlist))
# print(corpus)
# print(word2id)
# print(id2word)
# 윈도우 크기: 맥락의 크기(주변단어 몇개 포함여부)를 1로 한 경우
#           You say goodbye and I say hello .
# You        0   1     0     0  0       0   0
# say        1   0     1     0  1       1   0
# goodbye    0   1     0     1  0       0   0
# and        0   0     1     0  1       0   0
# i          0   1     0     1  0       0   0
# hello      0   1     0     0  0       0   1
# .          0   0     0     0  0       1   0
c = np.array([
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0]
])
print(c)
# print(id2word[0], '==> 를 벡터로 ' ,c[0])
# print(id2word[4], '==> 를 벡터로 ', c[4])
# print(c[word2id['goodbye']])
def corpus2matrix(corpus, wordsize, windowsize=1):
    result = np.zeros((wordsize, wordsize))
    for idx, wid in enumerate(corpus):
        print('idx, wid=', idx, wid)
        for i in range(1, windowsize+1):
            leftidx = idx - i
            rightidx = idx + i
            if leftidx >= 0:
                leftwordid = corpus[leftidx]
                result[wid, leftwordid] += 1
            if rightidx < len(corpus):
                rightwordid = corpus[rightidx]
                result[wid, rightwordid] += 1
    return result
c = corpus2matrix(corpus, 7)
print(c)

# 벡터사이의 유사도 - 코사인 유사도(-1~1 사이의 값), 유클리드 거리등
def cos_similarity(x, y, eps = 1e-8):
    nx = x / (np.sqrt(np.sum(x**2)) + eps)
    ny = y / (np.sqrt(np.sum(y**2)) + eps)
    return np.dot(nx, ny)
print('you와 i의 유사도=', cos_similarity(c[word2id['you']], c[word2id['i']]))

x = np.array([100,-5, 2])
print('x=',x)
print('x.argsort()=', x.argsort()) # 오름차순 정렬하여 배열의 인덱스 반환
print('(-x).argsort()=', (-x).argsort()) # 내림차순 정렬하여 배열의 인덱스 반환
# you 단어와 유사한 단어 5개 출력
corpus, word2id, id2word = preprocess(text)
def rank_similar(word, word2id, id2word, c, top=5):
    print('word=', word)
    print('wordid=', word2id[word])
    print('wordvec=', c[word2id[word]])
    sim = np.zeros(len(id2word))
    for i in range(len(id2word)):
        sim[i] = cos_similarity(c[i], c[word2id[word]])
    print('sim=', sim)
    print('내림차순 정렬=', (-1*sim).argsort()) # [0 2 4 5 1 3 6]
    cnt = 0
    for i in (-1*sim).argsort():
        if id2word[i] == word:
            continue
        print('{},{}'.format(id2word[i], sim[i]))
        cnt += 1
        if cnt >= top:
            return 

rank_similar('you',word2id, id2word, c)
