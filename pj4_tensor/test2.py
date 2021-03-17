import json
import urllib.request
from konlpy.tag import Okt 
from gensim.models import word2vec
# 시험 : 텍스트 데이터 분석

# 1) 네이버 api 활용하여 '추석' 유사도순으로 500건 블로그 검색, descript 항목 추출
with open ('C:\\myKey\\naver.txt') as f:
    pw = f.readline()
client_id = "tTUnbnTf9yFMsBYKKP5Q"
client_secret = pw
encText = urllib.parse.quote("추석")
url = "https://openapi.naver.com/v1/search/blog.json?start={}&display=100&query=" + encText # json 결과
for page in range(1,501,100):
    request = urllib.request.Request(url.format(page))
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8') 
        print("Error Code:" + rescode)
    dic = json.loads(result)
    with open('data/JiSeungwon.csv','a',encoding='utf-8') as f:
        for d in dic['items']: 
            desc = d['description']
            desc = desc.replace('<b>추석</b>', '추석')
            desc = desc.replace('...', ' ')
            print(desc)
            f.write(desc+'\n')

# 2) 형태소 분석 가장 많이 사용된 순으로 명사와 사용횟수 30개 출력
data = open('data/JiSeungwon.csv', encoding='utf-8').read()
fw = open('data/JiSeungwon2.csv', 'a', encoding='utf-8')
lines = data.split('\n')
okt = Okt()
maldic = {}
for line in lines:
    malist = okt.pos(line)
    templist = []
    for mal in malist:
        if mal[1] not in ['Alpha','Punctuation','Josa','Number','Emoi','Foreign']:
            templist.append(mal[0])
    malist_nouns = okt.nouns(line)
    fw.write(' '.join(templist))
    for mal in malist_nouns:
        if mal not in maldic:
            maldic[mal] = 0
        maldic[mal] = maldic[mal] + 1 
nlist = sorted(maldic.items(),key=lambda x:x[1],reverse=True)     
print("가장 많이 사용된 명사 30개")
rank = 1
for n in nlist[:30]:
    print(f'{rank}위',n[0])
    rank += 1

# 3) 형태소 분석 및 Word2Vec 모델 생성
data = word2vec.LineSentence('data/JiSeungwon2.csv') 
model = word2vec.Word2Vec(data, size=200, window=5, min_count=2, sg=1)
model.save('data/JiSeungwon2.model')

# 4) 생성된 모델 활용해 '선물'의 유사어를 출력
model = word2vec.Word2Vec.load('data/JiSeungwon2.model')
print('선물과 유사한 단어:',model.most_similar('선물', topn=5))