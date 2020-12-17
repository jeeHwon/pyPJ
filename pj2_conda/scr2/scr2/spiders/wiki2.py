import scrapy


# class Wiki2Spider(scrapy.Spider):
#     name = 'wiki2'
#     allowed_domains = ['wikibook.co.kr/list/']
#     start_urls = ['https://wikibook.co.kr/list//']

#     def parse(self, response):
#         # print(response.status)
#         #book-list > li:nth-child(1) > div.col-md-11.book-list-detail > a 
#         #book-list > li:nth-child(2) > div.col-md-11.book-list-detail > a
#         booklist = response.css('.book-url')
#         for a in booklist:
#             href = a.css('::attr(href)').get()
#             title = a.css('h4::text').get()
#             print(href, title)
#             yield{
#                 'url':href,
#                 'title':title
#             }
#             # scrapy crawl wiki2 -o wiki.csv --nolog
#             # scrapy crawl wiki2 -o wiki.json --nolog

class Wiki2Spider(scrapy.Spider):
    name = 'wiki2'
    allowed_domains = ['wikibook.co.kr']
    start_urls = ['https://wikibook.co.kr/list/']
    def parse(self, response):
        booklist = response.css('.book-url')
        for a in booklist[:3]:
            href = a.css('::attr(href)').get()
            print(href)
            # yield response.follow(url,메서드)
            yield response.follow(href,self.bookDetail)
    def bookDetail(self,response):   #상세페이지크롤링
        # print(response.status,'*'*30)
        imgurl = response.css('div.col-md-3.single-cover > a > img::attr(src)').get()
        title = response.css('div.col-md-9 > h1::text').get()
        filename = title + imgurl[-4:]
        # scrapy.Request(url,메서드)
        req=scrapy.Request(imgurl,self.saveImg)
        req.meta['filename'] = filename
        yield req
        # print(filename)
        # author=response.css('#content div.col-md-9 > ul > li:nth-child(3)::text').get()
        # print(imgurl,title,author)

    def saveImg(self,response):
        # print(response.meta['filename'],'***')
        fname = response.meta['filename']
        with open(fname, 'wb') as f:
            f.write(response.body)

# 과제
# http://movie.naver.com/movie/running/current.nhn에서
# 영화제목 네티즌점수 예매율을 수집하여 이름.csv 로 저장
# 제출시 파이썬 파일과 이름.csv