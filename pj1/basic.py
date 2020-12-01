import logging
# 프로그램 운영시 중요한 부분을 로그로 남기는것
# 단순한 에러인지 출력인지등을 관리하는 모듈
# logger.setLevel(logging.DEBUG)   #필요한 정보를 기록
# logger.setLevel(logging.INFO)    #정보알림
# logger.setLevel(logging.WARNING) #작동은 하지만 예상치 못한일이 발생할 것으로 예측
# logger.setLevel(logging.ERROR)   #에러
# logger.setLevel(logging.CRITICAL #심각한 오류


# 1. 로거 생성
logger = logging.getLogger('테스트')
logger.setLevel(logging.DEBUG)  # 1-2 레벨 설정

# 2. 파일 핸들러 생성
f1 = logging.FileHandler('data\\defalut.log', encoding='utf-8')
f2 = logging.FileHandler('data\\secret.log', encoding='utf-8')

# 2-2 레벨 설정(f2는 warning 부터 보겠다)
f2.setLevel(logging.WARNING)

logger.addHandler(f1)
logger.addHandler(f2)

# 3. 포매터 생성
# acstime 로깅발생 시간 level 은 위 다섯개중 하나 message는 내가 만들어
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
f1.setFormatter(formatter)
f2.setFormatter(formatter)

logger.debug('프로그램 디버그')
logger.info('프로그램 인포')
logger.warning('경고경고')
logger.error('에러발생')
logger.critical('심각한오류')
