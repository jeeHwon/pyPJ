import sys, ctypes
import win32com.client
import pandas as pd
from datetime import datetime
from slacker import Slacker
import time
from urllib.request import urlopen
import csv

# ======================== ver 3.06 ========================
# 201214~201218 분석 : 손절라인 무용, 최적 익절라인 분석

# 업데이트 내용 : 
# 1) myApp/env32/TodayResult.py로 금일 체결내역 myData/STResult에 csv로 저장
# 2) myApp/env64/TodayFramer.py로 csv 파일 읽어 가공하여 myData/STStatus에 csv로 저장
# 3) myApp/env64/myCal.py로 최적 익절라인 및 손절라인 분석
# 4) 익절라인 조정 : 1.5 -> 2.2%
# 5) 손절라인 조정 : 3.0 -> 20.0%
# target : 10
# price percent : 0.098
# target_buy_price = today_open + (lastday_high - lastday_low) * 0.5
# list = [ETF static] + [BB_TF] 
# target_sell_price
#   - pointDdan = 2.2%
#   - pointSonjul = -20.0%

# 로그 메시지 출력
def getPwd():
    """텍스트 파일을 읽어 비밀번호 또는 코드를 입력한다."""
    with open ('C:\\myKey\\slackbot.txt') as f:
        pw = f.readline()
    return pw.strip()
slack = Slacker(getPwd())

def dbgout(message):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S]') + message
    slack.chat.post_message('#general', strbuf)

def printlog(message, *args):
    """인자로 받은 문자열을 파이썬 셸에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message, *args)


# 크레온 플러스 공통 오브젝트
cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')  # 종목코드
cpStatus  = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')  # 주문관련
cpStock = win32com.client.Dispatch("DsCbo1.StockMst")
cpOhlc = win32com.client.Dispatch("CpSysDib.StockChart")
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')    # 계좌 정보
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')   # 주문 가능 금액
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 


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

    # 주문 관련 초기화 - 계좌 관련 코드가 있을 때만 사용
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system() : init trade -> FAILED')
        return False
    return True

# 현재가 조회
def get_current_price(code):
    """인자로 받은 종목의 현재가, 매수호가, 매도호가를 반환한다."""
    cpStock.SetInputValue(0, code)
    cpStock.BlockRequest()
    item = {}
    item['cur_price'] = cpStock.GetHeaderValue(11)  #현재가
    item['ask'] = cpStock.GetHeaderValue(16)        #매수호가
    item['bid'] = cpStock.GetHeaderValue(17)        #매도호가
    return item['cur_price'], item['ask'], item['bid']


# OHLC 조회
def get_ohlc(code, qty):
    """인자로 받은 종목의 OHLC 가격 정보를 qty 개수만큼 반환한다."""
    cpOhlc.SetInputValue(0, code)               # 종목코드
    cpOhlc.SetInputValue(1, ord('2'))           # 1:기간, 2:개수
    cpOhlc.SetInputValue(4, qty)                # 요청 개수
    cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5])    # 0:날짜, 2~5 OHLC
    cpOhlc.SetInputValue(6, ord('D'))           # D: 일단위
    cpOhlc.SetInputValue(9, ord('1'))           # 0: 무수정주가, 1:수정주가
    cpOhlc.BlockRequest()
    count = cpOhlc.GetHeaderValue(3)            # 3: 수신 개수
    columns = ['open', 'high', 'low', 'close']
    index = []
    rows = []
    for i in range(count):
        index.append(cpOhlc.GetDataValue(0, i))
        rows.append([cpOhlc.GetDataValue(1, i), cpOhlc.GetDataValue(2, i),
            cpOhlc.GetDataValue(3, i), cpOhlc.GetDataValue(4, i)])
    df = pd.DataFrame(rows, columns=columns, index=index)
    return df


# 주식 잔고 조회
def get_stock_balance(code):
    """인자로 받은 종목의 종목명과 수량을 반환한다."""
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
    accFlag = cpTradeUtil.GoodsList(acc, 1) # -1: 전체, 1:주식, 2:선물/옵션
    cpBalance.SetInputValue(0, acc)         # 계좌번호
    cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식상품 중 첫번째
    cpBalance.SetInputValue(2, 50)          # 요청건수(최대50)
    cpBalance.BlockRequest()
    if code == 'ALL':
        dbgout('계좌명: ' + str(cpBalance.GetHeaderValue(0)))
        dbgout('결제잔고수량: ' + str(cpBalance.GetHeaderValue(1)))
        dbgout('평가금액: ' + str(cpBalance.GetHeaderValue(3)))
        dbgout('평가손익: ' + str(cpBalance.GetHeaderValue(4)))
        dbgout('종목수: ' + str(cpBalance.GetHeaderValue(7)))
    stocks = []
    for i in range(cpBalance.GetHeaderValue(7)):
        stock_code = cpBalance.GetDataValue(12, i)  # 종목코드
        stock_name = cpBalance.GetDataValue(0, i)   # 종목명
        stock_qty = cpBalance.GetDataValue(15, i)   # 수량
        if code == 'ALL':
            dbgout(str(i+1)+' '+stock_code+'('+stock_name+')'+':'+str(stock_qty))
            stocks.append({'code': stock_code, 'name': stock_name, 'qty': stock_qty})
        if stock_code == code:
            return stock_name, stock_qty
    if code == 'ALL':
        return stocks
    else:
        stock_name = cpCodeMgr.CodeToName(code)
        return stock_name, 0


# 주문 가능 금액 조회
def get_current_cash():
    """증거금 100% 주문 가능 금액을 반환한다."""
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
    accFlag = cpTradeUtil.GoodsList(acc, 1) # -1: 전체, 1:주식, 2:선물/옵션
    cpCash.SetInputValue(0, acc)            # 계좌번호
    cpCash.SetInputValue(1, accFlag[0])     # 상품구분 - 주식상품 중 첫번째
    cpCash.BlockRequest()
    return cpCash.GetHeaderValue(9)         # 증거금 100% 주문 가능 금액


# 매수 목표가 계산
def get_target_price(code):
    """매수 목표가를 반환한다."""
    try:
        time_now = datetime.now()
        str_today = time_now.strftime('%Y%m%d')
        ohlc = get_ohlc(code, 10)
        if str_today == str(ohlc.iloc[0].name):
            today_open = ohlc.iloc[0].open
            lastday = ohlc.iloc[1]
        else:
            lastday = ohlc.iloc[0]
            today_open = lastday[3]
        lastday_high = lastday[1]
        lastday_low = lastday[2]
        target_price = today_open + (lastday_high - lastday_low) * 0.5
        return target_price
    except Exception as ex:
        dbgout("'get_target_price() -> exception!" + str(ex)+"'")
        return None


# 이동평균값 조회
def get_movingaverage(code, window):
    """인자로 받은 종목에 대한 이동평균가격을 반환한다. 최대 40일"""
    try:
        time_now = datetime.now()
        str_today = time_now.strftime('%Y%m%d')
        ohlc = get_ohlc(code, 40)
        if str_today == str(ohlc.iloc[0].name):
            lastday = ohlc.iloc[1].name
        else:
            lastday = ohlc.iloc[0].name
        closes = ohlc['close'].sort_index()
        ma = closes.rolling(window=window).mean()
        return ma.loc[lastday]
    except Exception as ex:
        dbgout('get_movingaverage() -> exception!' + str(ex)+"")
        return None

# 크레온 데이터 조회
obj = win32com.client.Dispatch("DsCbo1.StockMst")
obj.SetInputValue(0, 'A005930')
obj.BlockRequest()
sec = {}
sec['현재가'] = obj.GetHeaderValue(11)
sec['전일대비'] = obj.GetHeaderValue(12)


# 최유리 FOK 매수 주문
def buy_etf(code):
    """인자로 받은 종목을 최유리 지정가 FOK 조건으로 매수한다."""
    try:
        global bought_list      # 함수 내에서 값 변경을 하기 위해 global로 지정
        if code in bought_list: # 매수 완료 종목이면 더 이상 안 사도록 함수 종료
            printlog('code:', code, 'in', bought_list) 
            return False
        time_now = datetime.now()
        current_price, ask_price, bid_price = get_current_price(code)
        target_price = get_target_price(code)       # 매수 목표가
        ma5_price = get_movingaverage(code, 5)      # 5일 이동평균가
        ma10_price = get_movingaverage(code, 10)    # 10일 이동평균가
        buy_qty = 0         # 매수할 수량 초기화
        if ask_price > 0:   # 매수호가가 존재하면
            buy_qty = buy_amount // ask_price
        stock_name, stock_qty = get_stock_balance(code) # 종목명과 보유수량 조회
        printlog('bought_list:', bought_list, 'len(bought_list):',
            len(bought_list), 'target_buy_count:', target_buy_count)

        if current_price > target_price and current_price > ma5_price and current_price > ma10_price:
            printlog(stock_name+'('+str(code)+')'+str(buy_qty)+'EA : '+str(current_price)+'meets the buy condition!')
            cpTradeUtil.TradeInit()
            acc = cpTradeUtil.AccountNumber[0]
            accFlag = cpTradeUtil.GoodsList(acc, 1)

            # 최유리 FOK 매수 주문
            cpOrder.SetInputValue(0, "2")           # 1:매도, 2:매수
            cpOrder.SetInputValue(1, acc)           # 계좌번호
            cpOrder.SetInputValue(2, accFlag[0])    # 상품구분 - 주식상품 중 첫번째
            cpOrder.SetInputValue(3, code)          # 종목코드
            cpOrder.SetInputValue(4, buy_qty)       # 매수할 수량
            cpOrder.SetInputValue(7, "2")           # 주문조건 0:기본, 1:IOC 2:FOK
            cpOrder.SetInputValue(8, "12")          # 주문호가 1:보통, 3:시장가, 5:조건부, 12:최유리, 13:최우선

            # 매수 주문 요청
            ret = cpOrder.BlockRequest()
            printlog('최유리 FOK 매수 ->', stock_name, code, buy_qty, '->', ret)
            if ret == 4:
                remain_time = cpStatus.LimitRequestRemainTime
                printlog('주의: 연속 주문 제한에 걸림. 대기시간:', remain_time/1000)
                time.sleep(remain_time/1000)
                return False
            time.sleep(2)
            printlog('종목별 주문 금액 :', buy_amount)
            stock_name, bought_qty = get_stock_balance(code)
            printlog('get_stock_balance :', stock_name, stock_qty)
            if bought_qty > 0:
                bought_list.append(code)
                dbgout("'buy_stock("+ str(stock_name) + " : "+str(code)+") -> "+str(bought_qty)+ "EA bought!"+"'")
    except Exception as ex:
        dbgout("'buy_stock(" + str(code)+ ") -> exception!" + str(ex) +"'")


# 최유리 IOC 매도 주문
def sell_all():
    """보유한 모든 종목을 최유리 지정가 IOC 조건으로 매도한다."""
    try:
        cpTradeUtil.TradeInit()
        acc = cpTradeUtil.AccountNumber[0]          # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1)     # -1:전체, 1:주식, 2:선물/옵션
        while True:
            stocks = get_stock_balance('ALL')
            total_qty = 0
            for s in stocks:
                total_qty += s['qty']
            if total_qty == 0:
                return True
            for s in stocks:
                if s['qty'] != 0:
                    cpOrder.SetInputValue(0, "1")
                    cpOrder.SetInputValue(1, acc)
                    cpOrder.SetInputValue(2, accFlag[0])
                    cpOrder.SetInputValue(3, s['code'])
                    cpOrder.SetInputValue(4, s['qty'])
                    cpOrder.SetInputValue(7, "1")
                    cpOrder.SetInputValue(8, "12")

                    #최유리 IOC 매도 주문 요청
                    ret = cpOrder.BlockRequest()
                    printlog('최유리 IOC 매도', s['code'], s['name'], s['qty'], '-> cpOrder.BlockRequest() ->returned', ret)
                    if ret == 4:
                        remain_time = cpStatus.LimitRequestRemainTime
                        printlog('주의: 연속 주문 제한,대기시간:', remain_time/1000)
                time.sleep(1)
            time.sleep(30)
    except Exception as ex:
        dbgout("sell_all() -> exception! "+str(ex)) 


def sell_etf():
    """수익률이 일정 퍼센트 이상 또는 이하 종목을 최유리 지정가 IOC 조건으로 매도한다."""
    try:
        global bought_list
        pointDdan = 2.2
        pointSonjul = -20.0
        cpTradeUtil.TradeInit()
        acc = cpTradeUtil.AccountNumber[0]          # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1)     # -1:전체, 1:주식, 2:선물/옵션
        cpBalance.SetInputValue(0, acc)         # 계좌번호
        cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식상품 중 첫번째
        cpBalance.SetInputValue(2, 50)          # 요청건수(최대50)
        cpBalance.SetInputValue(3, "2")         # 수익률 "1":100%기준, "2":0%기준
        cpBalance.BlockRequest()

        printlog('bought_list:', bought_list, 'len(bought_list):',
            len(bought_list), 'target_buy_count:', target_buy_count)

        for i in range(cpBalance.GetHeaderValue(7)):
            stock_code = cpBalance.GetDataValue(12, i)  # 종목코드
            stock_name = cpBalance.GetDataValue(0, i)   # 종목명
            stock_qty = cpBalance.GetDataValue(15, i)   # 수량
            stock_returns = cpBalance.GetDataValue(11, i)   # 수익률
            # s = {'code': stock_code, 'name': stock_name, 'qty': stock_qty}
            if stock_returns > pointDdan or stock_returns < pointSonjul:# 수익률 특정 퍼센트 이상 이하일 때 매도 
                cpOrder.SetInputValue(0, "1")           # 1:매도, 2:매수
                cpOrder.SetInputValue(1, acc)           # 계좌번호
                cpOrder.SetInputValue(2, accFlag[0])    # 주식상품 중 첫번째
                cpOrder.SetInputValue(3, stock_code)    # 종목코드
                cpOrder.SetInputValue(4, stock_qty)     # 매도수량
                cpOrder.SetInputValue(7, "1")           # 조건 0:기본, 1:IOC, 2:FOK
                cpOrder.SetInputValue(8, "12")          # 호가 12:최유리, 13:최우선
                # 최유리 IOC 매도 주문 요청
                ret = cpOrder.BlockRequest()
                printlog('최유리 IOC 매도', stock_code, stock_name, stock_qty, '-> cpOrder.BlockRequest() ->returned', ret)
                dbgout("'sell_etf("+ str(stock_name) + " : "+str(stock_code)+") -> "+str(stock_qty)+ "EA sold!"+"'")
                time.sleep(1)
                if ret == 4:
                    remain_time = cpStatus.LimitRequestRemainTime
                    printlog('주의: 연속 주문 제한,대기시간:', remain_time/1000)
                bought_list.remove(stock_code)

    except Exception as ex:
        dbgout("sell_etf() -> exception! "+str(ex))

# 메인로직
if __name__ == '__main__': 
    try:
        # ETF 후보 리스트
        symbol_list = ['A122630', 'A252670', 'A233740', 'A250780', 'A225130', 'A280940', 'A261220', 'A217770', 'A295000', 'A176950']

        # 볼린저밴드 추세추종 해당 종목 추가 
        with open('C:/myApp/env64/BB_TF_buylist.csv', 'r', encoding='utf-8') as f:
            rdr = csv.reader(f) 
            for i,line in enumerate(rdr): 
                if i==0: 
                    symbol_list.extend(line)

        # 볼린저밴드 반전매매 해당 종목 추가 
        with open('C:/myApp/env64/BB_RV_buylist.csv', 'r', encoding='utf-8') as f:
            rdr = csv.reader(f) 
            for i,line in enumerate(rdr): 
                if i==0: 
                    symbol_list.extend(line)

        bought_list = []     # 매수 완료된 종목 리스트
        target_buy_count = 10 # 매수할 종목 수
        buy_percent = 0.098
        printlog('check_creon_system() :', check_creon_system())  # 크레온 접속 점검
        stocks = get_stock_balance('ALL')      # 보유한 모든 종목 조회
        total_cash = int(get_current_cash())   # 100% 증거금 주문 가능 금액 조회
        buy_amount = total_cash * buy_percent  # 종목별 주문 금액 계산
        printlog('100% 증거금 주문 가능 금액 :', total_cash)
        printlog('종목별 주문 비율 :', buy_percent)
        printlog('종목별 주문 금액 :', buy_amount)
        printlog('오늘 리스트업 된 종목수 :', len(symbol_list))
        printlog('시작 시간 :', datetime.now().strftime('%m/%d %H:%M:%S'))
        # time.sleep(10)
        soldout = False;
        
        while True:
            t_now = datetime.now()
            t_9 = t_now.replace(hour=9, minute=0, second=0, microsecond=0)
            t_start = t_now.replace(hour=9, minute=5, second=0, microsecond=0)
            t_buyonly = t_now.replace(hour=9, minute=10, second=0, microsecond=0)
            t_sell = t_now.replace(hour=15, minute=15, second=0, microsecond=0)
            t_exit = t_now.replace(hour=15, minute=20, second=0,microsecond=0)
            today = datetime.today().weekday()
            if today == 5 or today == 6:  # 토요일이나 일요일이면 자동 종료
                printlog('Today is', 'Saturday.' if today == 5 else 'Sunday.')
                sys.exit(0)
            if t_9 < t_now < t_start and soldout == False:
                soldout = True
                sell_all()
            if t_start < t_now < t_buyonly :  # AM 09:05 ~ AM 09:10 : 집중매수
                for sym in symbol_list:
                    if len(bought_list) < target_buy_count:
                        buy_etf(sym)
                        time.sleep(0.5)
            if t_buyonly < t_now < t_sell :  # AM 09:10 ~ PM 03:15 : 매수 및 매도
                for sym in symbol_list:
                    if len(bought_list) < target_buy_count:
                        buy_etf(sym)
                        time.sleep(1)
                sell_etf()
                time.sleep(1)
                if t_now.minute == 30 and 0 <= t_now.second <= 10: 
                    get_stock_balance('ALL')
                    time.sleep(10)
            if t_sell < t_now < t_exit:  # PM 03:15 ~ PM 03:20 : 일괄 매도
                if sell_all() == True:
                    dbgout('`sell_all() returned True -> self-destructed!`')
                    sys.exit(0)
            if t_exit < t_now:  # PM 03:20 ~ :프로그램 종료
                dbgout('`self-destructed!`')
                sys.exit(0)
            time.sleep(3)
    except Exception as ex:
        dbgout('`main -> exception! ' + str(ex) + '`')
