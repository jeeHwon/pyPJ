import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['http://alexa.com/topsites/']

    def parse(self, response):
        # print(response.body)
        # print(response.status)  #200

        # response.css('셀렉터').get() or response.css('셀렉터').getall()

        #site 이름만 뽑기
        #alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child(2) > div.td.DescriptionCell > p > a
        #div.listings.table > div.td.DescriptionCell > p > a
        # aes = response.css('div.listings.table  div.td.DescriptionCell > p > a').getall()
        # for a in aes:
        #     yield {
        #         'sitename':a
        #     }
        # scrapy crawl test1 -o alexa.json --nolog

        # 하나의 모든내용 뽑기
        #alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child(2) > div.td.DescriptionCell > p > a
        #alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child(2) > div:nth-child(3) > p
        # tr = response.css('div.listings.table > div:nth-child(2)')
        # rank = tr.css('.td::text').get() + '위'
        # name = tr.css('.DescriptionCell a::text').get()
        # time = tr.css('.td.right p::text').getall()[0]
        # visitor = tr.css('.td.right p::text').getall()[1]
        # search = tr.css('.td.right p::text').getall()[2]
        # link = tr.css('.td.right p::text').getall()[3]
        # print(rank, name, time, visitor, search, link)

        # 전체의 모든내용 뽑기
        trs = response.css('div.listings.table > div.tr.site-listing')
        for tr in trs:
            rank = tr.css('.td::text').get() + '위'
            name = tr.css('.DescriptionCell a::text').get()
            time = tr.css('.td.right p::text').getall()[0]
            visitor = tr.css('.td.right p::text').getall()[1]
            search = tr.css('.td.right p::text').getall()[2]
            link = tr.css('.td.right p::text').getall()[3]
            yield {
                'rank':rank,
                'name':name,
                'time':time,
                'visitor':visitor,
                'search':search,
                'link':link
            }
            print(rank, name, time, visitor, search, link)
            
        # for a in aes:
        #     yield {
        #         'sitename':a
        #     }
        # scrapy crawl test1 -o JiSeungwon.csv --nolog