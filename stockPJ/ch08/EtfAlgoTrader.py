import ctypes
import win32com.client

# 크레온 플러스 공통 오브젝트
cpStatus  = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')

# 크레온 플러스 시스템 점검 함수
def check_creon_system():
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('check_creon_system() : admin user -> FAILED')
        return False

    # 연결여부 체크
    if (cpStatus.IsConnect == 0):
        print('check_creon_system() : connect to server -> FAILED')
        return False

    # 주문 관련 초기화
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system() : init trade -> FAILED')
        return False
    
    return True

# 크레온 데이터 조회
obj = win32com.client.Dispatch("DsCbo1.StockMst")
obj.SetInputValue(0, 'A005930')
obj.BlockRequest()
sec = {}
sec['현재가'] = obj.GetHeaderValue(11)
sec['전일대비'] = obj.GetHeaderValue(12)

# 로그 메시지 출력
from slacker import Slacker
from datetime import datetime

def getPwd():
    with open ('C:\\myKey\\slackbot.txt') as f:
        pw = f.readline()
    return pw.strip()
slack = Slacker(getPwd())
def dbgout(message):
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S]') + message
    slack.chat.post_message('#general', strbuf)

def printlog(message, *args):
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message, *args)