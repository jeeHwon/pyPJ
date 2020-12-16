import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikibook.co.kr/list/']
    start_urls = ['http://wikibook.co.kr/list//']

    def parse(self, response):
        # print(response.status)
        #book-list > li:nth-child(1) > div.col-md-11.book-list-detail > a > h4
        book = response.css('div.col-md-11.book-list-detail > a > h4').get()
        # print(book)
        book_href = response.css('div.col-md-11.book-list-detail > a::attr(href)').get()
        # print(book_href)
        book_name = response.css('div.col-md-11.book-list-detail > a > h4::text').get()
        # print(book_name)
        yield{
            'title':book_name,
            'bookurl':book_href
        }
        # scrapy crawl wiki --nolog -o wiki.json
        # scrapy crawl wiki --nolog -o wiki.csv