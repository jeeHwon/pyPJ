# korea news crawler
# https://github.com/lumyjuwon/KoreaNewsCrawler
# pip install KoreaNewsCrawler

from korea_news_crawler.articlecrawler import ArticleCrawler
from multiprocessing import freeze_support
if __name__ =='__main__':
    freeze_support()
    c = ArticleCrawler()
    c.set_category('IT과학')
    c.set_date_range(2021, 1, 2021, 2)  
    c.start()