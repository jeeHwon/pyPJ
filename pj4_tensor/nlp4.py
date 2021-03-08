from konlpy.tag import Okt 
# 많이 사용된 명사 30개 추출
# {'꽃':10, '나무':8...}
# data = open('data/news.csv', encoding='utf-8').read()
# lines = data.split('\n')
# okt = Okt()
# maldic = {}
# for line in lines:
#     malist = okt.nouns(line)
#     # print(malist)
#     for mal in malist:
#         if mal not in maldic:
#             maldic[mal] = 0
#         maldic[mal] = maldic[mal] + 1            
# # print(sorted(maldic.items(),reverse=True))
# nlist = sorted(maldic.items(),key=lambda x:x[1],reverse=True)
# print(nlist[:30])
# for n in nlist[:30]:
#     print(n[0], end=' ')

# 단어 전처리 해 저장
# data = open('data/news.csv', encoding='utf-8').read()
# fw = open('data/news3.csv', 'a', encoding='utf-8')
# lines = data.split('\n')
# okt = Okt()
# maldic = {}
# for line in lines:
#     malist = okt.pos(line)
#     templist = []
#     for mal in malist:
#         if mal[1] not in ['Alpha','Punctuation','Josa','Number','Emoi','Foreign']:
#             templist.append(mal[0])
#     print(templist)
#     fw.write(' '.join(templist))

from gensim.models import word2vec
# data = word2vec.LineSentence('data/news3.csv') # 단어 단어 단어
# model = word2vec.Word2Vec(data, size=200, window=5, min_count=2, sg=1)
# model.save('data/news2.model')

# model = word2vec.Word2Vec.load('data/news2.model')
# print(model.most_similar('노래', topn=3))



# 1)네이버 api를 활용- 블러그에서 성탄절을 검색하여  description의 내용을 500건 수집하여 blog.csv로 저장
# 2) 가장 많이 사용된 명사 10개와 그 횟수 출력
# 3)'선물'과 유사한 단어 출력
# import json
# import urllib.request
# with open ('C:\\myKey\\naver.txt') as f:
#     pw = f.readline()
# client_id = "tTUnbnTf9yFMsBYKKP5Q"
# client_secret = pw
# encText = urllib.parse.quote("성탄절")
# url = "https://openapi.naver.com/v1/search/blog.json?start={}&display=100&query=" + encText # json 결과
# for page in range(1,1001,100):
#     request = urllib.request.Request(url.format(page))
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request)
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         # print(response_body.decode('utf-8'))
#         result = response_body.decode('utf-8') # json
#     else:
#         print("Error Code:" + rescode)
#     dic = json.loads(result)
#     # print(dic)
#     with open('data/blog.csv','a',encoding='utf-8') as f:
#         for d in dic['items']: # [{}, {}, {}..]
#             desc = d['description']
#             desc = desc.replace('<b>성탄절</b>', '성탄절')
#             desc = desc.replace('...', ' ')
#             print(desc)
#             f.write(desc+'\n')

# data = open('data/blog.csv', encoding='utf-8').read()
# fw = open('data/blog2.csv', 'a', encoding='utf-8')
# lines = data.split('\n')
# okt = Okt()
# maldic = {}
# for line in lines:
#     malist = okt.pos(line)
#     templist = []
#     for mal in malist:
#         if mal[1] not in ['Alpha','Punctuation','Josa','Number','Emoi','Foreign']:
#             templist.append(mal[0])
#     malist_nouns = okt.nouns(line)
#     fw.write(' '.join(templist))
#     for mal in malist_nouns:
#         if mal not in maldic:
#             maldic[mal] = 0
#         maldic[mal] = maldic[mal] + 1 
# nlist = sorted(maldic.items(),key=lambda x:x[1],reverse=True)     
# for n in nlist[:30]:
#     print(n[0], end=' ')

data = word2vec.LineSentence('data/blog2.csv') 
model = word2vec.Word2Vec(data, size=200, window=5, min_count=2, sg=1)
model.save('data/blog2.model')

model = word2vec.Word2Vec.load('data/blog2.model')
print('선물과 유사한 단어',model.most_similar('선물', topn=3))