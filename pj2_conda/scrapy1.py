# 스크래피
# 아나콘다 - 특정 용도의 소프트웨어 패키지를 묶어서 제공

# pip install scrapy

# 1) 스크래피 프로젝트 생성
# scrapy startproject 프로젝트명
# scrapy startproject scr1

# 2-1)스파이더 생성 -> 같은이름의 폴더 2개 생성됨
# cd scr1 --scrapy.cfg 파일이 있는 곳에서 명령어를 실행
# scrapy genspider 스파이더이름 수집할도메인
# scrapy genspider test1 alexa.com/topsites

# 2-2)스파이더 생성
# scrapy genspider test2 movie.naver.com/movie/running/currnt.nhn
# scrapy genspider mov movie.naver.com/movie/running/currnt.nhn


# 2-3)스파이더 생성
# scrapy genspider wiki wikibook.co.kr/list/
# scrapy genspider wiki2 wikibook.co.kr/list/

# 3-1)크롤링
# scrapy crawl 스파이더이름
# scrapy crawl test1
# scrapy crawl test1 --nolog  #로그 없이 실행
# ---scr1.spider.test1 편집(http->https로 상관없는데 걍 해줬어)
# ---settings.py에 
#         robotstxt_obey = true => false로 수정 (robot.txt 때문에 안되는거 방지)
#         FEED_EXPORT_ENCODING='utf-8'    (추가해서 한글처리)

# 메서드   get(), extract_first()     --1개만 가져오기
#         getall(), extract()        --다가져오기

# 3-2)실행해 파일로 저장
# scrapy crawl test1 -o alexa.json
# scrapy crawl test1 -o alexa.json --nolog
# scrapy crawl test1 -o alexa.csv --nolog