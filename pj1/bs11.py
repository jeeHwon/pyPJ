# 만개의 레시피에서 밑반찬 레시피를 recipe.txt로 저장
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from tqdm import trange

def saveData(title, result):
    with open('D:\\study\\pj1\\data\\recipe.txt', 'a', encoding='utf-8') as f:
        str = '\n===={}====\n--조리순서--'.format(title)
        f.write(str+'\n')
        for k, v in result.items():
            str = "{} : {}".format(k, v)
            f.write(str+'\n')


def makeData(pageUrl):
    r = requests.get(pageUrl)
    d = BeautifulSoup(r.text, 'lxml')
    title = d.find('div', class_='view2_summary st3').find('h3').text
    title = title.replace('\n', '')
    stepDivs = d.findAll('div', class_='view_step_cont')
    steplist = []
    for div in stepDivs:
        step = div.find('div', class_='media-body').text
        step = step.replace('\n', '')
        steplist.append(step)
    # print(steplist)
    index = []
    for i in range(len(steplist)):
        index.append(i+1)
    # print(index)
    result = {}
    for k, v in zip(index, steplist):
        result[k] = v
    saveData(title, result)
    


    
for page in range(1, 2):
    url = 'https://www.10000recipe.com/recipe/list.html?q=%EB%B0%91%EB%B0%98%EC%B0%AC&order=reco&page={}'.format(page)
    recvd = requests.get(url)
    dom = BeautifulSoup(recvd.text, 'lxml')
    divs = dom.find_all('div', class_='common_sp_thumb')

    for div in divs:
        # pageUrl = 'https://sports.news.naver.com'+a['href']
        # https://www.10000recipe.com/recipe/6886357
        pageUrl = 'https://www.10000recipe.com'+ div.find('a')['href']
        # print(pageUrl)
        makeData(pageUrl)
        

# ===============선생님버전


# # import requests
# # from bs4 import BeautifulSoup
# # url='https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
# # recvd=requests.get(url)
# # # print(recvd)
# # dom=BeautifulSoup(recvd.text,'lxml')
# # lis=dom.find_all('li',{'class':"common_sp_list_li"})
# # # print(len(lis))
# # for li in lis:
# #     # print(li)
# #     pageUrl='https://www.10000recipe.com'+li.find('a')['href']
# #     print(pageUrl)
#
#
# import requests
# from bs4 import BeautifulSoup
# url='https://www.10000recipe.com/recipe/6912734'
# recvd=requests.get(url)
# dom=BeautifulSoup(recvd.text,'lxml')
# title=dom.find('div',class_="view2_summary st3").find('h3').text
# # print(title)
# # 재료
# view_step=dom.find('div',class_='view_step')
# divs=view_step.find_all('div',{'class':"media-body"})
# # print(len(divs))
# # print(divs)
# i=0
# for div in divs:
#     i=i+1
#     print(str(i)+']'+div.text)
#----------------------
# import requests
# from bs4 import BeautifulSoup
# def makeContent(pageUrl):
#     recvd=requests.get(pageUrl)
#     dom=BeautifulSoup(recvd.text,'lxml')
#     title=dom.find('div',class_="view2_summary st3").find('h3').text
#     # 재료
#     view_step=dom.find('div',class_='view_step')
#     divs=view_step.find_all('div',{'class':"media-body"})
#     i=0
#     contents=[]
#     for div in divs:
#         i=i+1
#         contents.append(str(i)+']'+div.text)
#     print('{}\n\n조리순서\n{}'.format(title,'\n'.join(contents)))
# def main(url):
#     recvd=requests.get(url)
#     dom=BeautifulSoup(recvd.text,'lxml')
#     lis=dom.find_all('li',{'class':"common_sp_list_li"})
#     for li in lis:
#         pageUrl='https://www.10000recipe.com'+li.find('a')['href']
#         # print(pageUrl)
#         makeContent(pageUrl)
#         break
# url='https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
# if __name__=='__main__':
#     main(url)


