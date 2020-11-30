# from urllib.parse import *
# from bs4 import BeautifulSoup
# import urllib.request
# import os
# import re
# import time

# url = 'https://docs.python.org/3.8/library/'
# baseurl = urlparse(url)
# print('urlparse', baseurl)
# savepath = './'+baseurl.netloc+ baseurl.path
# print('savepath:',savepath)

# # if savepath[-1] == '/':
# #     print('directory')
# if re.search(r'/$', savepath):
#     savepath += 'index.html'
# print(savepath)
# if not os.path.exists(savepath):
#     os.makedirs(os.path.dirname(savepath))
# urllib.request.urlretrieve(url, savepath)
# time.sleep(1)

# html = open(savepath, encoding='utf-8').read()

# # 링크만 뽑아내기
# dom = BeautifulSoup(html, 'lxml')
# aes = dom.select('a')
# for a in aes:
#     pageurl = urljoin(url, a['href'])
#     print(a['href'], '==>', pageurl) 

# =======전체페이지로 확대해보기===================
from urllib.parse import *
from bs4 import BeautifulSoup
import urllib.request
import re
import os
import time

from bs4 import BeautifulSoup

def enum_link(html, base):
    dom = BeautifulSoup(html, 'lxml')
    links = dom.select('a')
    result = []
    for a in links:
        url = urljoin(base, a['href'])
        result.append(url)
    return result

def download_file(url):
    o = urlparse(url)
    savepath='./' + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += 'index.html'
    # print('savepath=',savepath)
    if not os.path.exists(os.path.dirname(savepath)):
        os.makedirs(os.path.dirname(savepath))
    try:
        urllib.request.urlretrieve(url, savepath)
        return savepath
    except:
        print('다운로드 오류', url)
        return None


def analyze_html(url, root_url):
    savepath = download_file(url)
    html = open(savepath, encoding='utf-8').read()
    links = enum_link(html, url)
    print(links)

# if __name__=='__main__':
#     url = 'https://docs.python.org/3.8/library/'
#     analyze_html(url, url)

a = 'blue green red'
print(a.find('red'))
print(a.find('blue'))
print(a.find('pink'))