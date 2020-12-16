import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['movie.naver.com/movie/running/currnt.nhn']
    start_urls = ['http://movie.naver.com/movie/running/currnt.nhn/']

    def parse(self, response):
        pass
