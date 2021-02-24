import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 파이썬 라이브러리 모음 페이지
# https://www.lfd.uci.edu/~gohlke/pythonlibs/
# wordcloud‑1.8.1‑cp36‑cp36m‑win_amd64.whl
# 받아서 pip install

# 워드 클라우드
# data = open('data/alice.txt').read()
# print(data)
# # wc = WordCloud().generate(data)
# wc = WordCloud(background_color='white', max_words=2000).generate(data)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()

# 마스크 적용
from PIL import Image
import numpy as np
from wordcloud import STOPWORDS

# 숨길 단어 설정
print(STOPWORDS)
sw = STOPWORDS
print(len(sw))
sw.add('said')
print(len(sw))

img = Image.open('img/one.png')
mask = np.array(img)
print(mask)
data = open('data/alice.txt').read().lower()
wc = WordCloud(mask=mask, stopwords=sw).generate(data)
plt.imshow(wc)
plt.axis('off')
plt.show()