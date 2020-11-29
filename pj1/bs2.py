from bs5 import BeautifulSoup
with open('data\\test.html', mode='r', encoding='utf-8') as f:
    text = f.read()
    # print(text)
    dom = BeautifulSoup(text, 'lxml')
    # div인 처번째 태그
    div = dom.find('div')
    # print(div)
    # div인 모든 태그
    divs = dom.find_all('div')
    # print(divs)

    # div 태그중에 클래스가 'ex_class'인것 모두 추출
    divs = dom.find('div', {'class': 'ex_class'})
    # print(divs)

    # 클래스가 'ex_class'인것 모두 추출
    divs = dom.find_all(class_='ex_class')
    # print(divs)

    # id가 'ex_id'인 것 추출
    ids = dom.find(id='ex_id')
    # print(ids)

    # id가 'ex_id'인 것중 모든 p태그 추출
    ps = ids.find_all('p')
    # print(ps)
    for s in ps:
        str = s.string
    #    print(str)

    # data 추출
    #   dom.string
    #   dom.text
    #   dom.get_text()

    title = dom.find('title')
    # print(title)
    # print(title.string)
    # print(title.text)
    # print(title.get_text())
    
    # a의 내용추출
    acon = dom.find_all('a')
    # print(acon) # list
    # for a in acon:
    #    print(a.text)

    # 속성 추출
    # dom['속성']
    # dom.get('속성')
    # dom.attr['속성']

    # for a in acon:
    #     print(a.text)
    #     print(a['href'])

    # id가 link2인 요소의 class 추출
    link2 = dom.find(id='link2')
    # print(link2['class'])

    # dom 추적
    # dom.parent 부모
    # dom.parents 조상, 객체로 반환
    # dom.children 자식
    # dom.descendants 자손

    title = dom.find('p', class_='title')
    # print(title)
    # print('-'*30)
    # print('parent', title.parent)
    # print('-' * 30)
    # print('parents', title.parents)
    # for p in title.parents:
    #     print(p)

    # id가 second인 div
    div = dom.find(id='second')
    # print(div)
    divchild = div.children
    # print(divchild) # list 객체
    # for c in divchild: #줄바꿈 까지 하나의 객체로 출력한다
    #     print(c)
    #     print('='*50)

    divdes = div.descendants
    # print(divdes)
    # for d in divdes:
    #     print(d)
    #     print('=' * 50)

    # id가 link2인 a의 형제찾기
    a = dom.find(id='link2')
    anext = a.next_siblings
    # print(anext)
    for a in anext:
        print(a)
        print('=' * 50)


