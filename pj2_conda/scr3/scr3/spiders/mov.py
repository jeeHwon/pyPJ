import scrapy


class MovSpider(scrapy.Spider):
    name = 'mov'
    allowed_domains = ['movie.naver.com/movie/running/current.nhn']
    start_urls = ['https://movie.naver.com/movie/running/current.nhn']

    def parse(self, response):
        list = response.css('.lst_detail_t1 > li')
        # print(len(list))

        for movie in list:
            title = movie.css('.tit > a::text').get()
            star = movie.css('.star_t1 .num::text').get()
            rate = movie.css('.b_star > .num::text').get()
            if rate==None:
                rate = 0
            # print(title, star, rate)
            yield{
                'title': title,
                'star': star,
                'rate': rate
            }
        # scrapy crawl mov -o JiSeungwon.csv --nolog

