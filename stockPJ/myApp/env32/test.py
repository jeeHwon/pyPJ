import sys, ctypes
import win32com.client
import pandas as pd
from datetime import datetime
from slacker import Slacker
import time
from urllib.request import urlopen
import csv
import os

cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')  # 종목코드
cpStatus  = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')  # 주문관련
cpStock = win32com.client.Dispatch("DsCbo1.StockMst")
cpOhlc = win32com.client.Dispatch("CpSysDib.StockChart")
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')    # 계좌 정보
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')   # 주문 가능 금액
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 
cpToday = win32com.client.Dispatch('CpTrade.CpTd5342') 
# date = "2020-12-14" 오늘 날짜 자동 최신화
date = datetime.today().strftime('%Y-%m-%d')

try:
    # 크레온 플러스 시스템 점검 함수
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('check_creon_system() : admin user -> FAILED')

    # 연결여부 체크
    if (cpStatus.IsConnect == 0):
        print('check_creon_system() : connect to server -> FAILED')

    # 주문 관련 초기화 - 계좌 관련 코드가 있을 때만 사용
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system() : init trade -> FAILED')


    # 계좌 받기
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0]
    accFlag = cpTradeUtil.GoodsList(acc, 1)

    # 1)금일 데이터인 경우
    # 금일 주문내역 받아오기
    cpToday.SetInputValue(0, acc)           # 계좌번호
    cpToday.SetInputValue(1, accFlag[0])    # 상품관리구분코드
    cpToday.SetInputValue(2, 20)            #
    cpToday.SetInputValue(3, "1")            # 


    columns = ['DATE', 'CODE', 'NAME', 'BUY', 'SELL', 'QTY', 'OPEN','HIGH', 'LOW', 'CLOSE']
    rows = []
    while True:
        cpToday.BlockRequest()
        print(cpToday.GetHeaderValue(8))
        count = cpToday.GetHeaderValue(8) # 수신 개수
        medo = cpToday.GetHeaderValue(9) # 수신 개수
        mesu = cpToday.GetHeaderValue(10) # 수신 개수

        # columns = ['DATE', 'CODE', 'NAME', 'BUY', 'SELL', 'RATE', 'RETURN', 'OPEN', 'HIGH', 'LOW', 'CLOSE']
        for i in range(count):
            if cpToday.GetDataValue(3, i) > 0:
                code = cpToday.GetDataValue(0, i)   # 종목코드
                name = cpToday.GetDataValue(1, i)   # 종목명
                qty = cpToday.GetDataValue(3, i)   # 종목명
                fee = cpToday.GetDataValue(4, i)   # 종목명
                nong = cpToday.GetDataValue(5, i)   # 종목명
                type1 = cpToday.GetDataValue(10, i)  #체결수량
                type2 = cpToday.GetDataValue(10, i)  #체결수량
                type3 = cpToday.GetDataValue(12, i)  #체결수량
                type4 = cpToday.GetDataValue(24, i)  #체결수량
                print(date, code, name, qty, fee, nong,type1,type2,type3,type4)

                # cpOhlc.SetInputValue(0, code)               # 종목코드
                # cpOhlc.SetInputValue(1, ord('2'))           # 1:기간, 2:개수
                # cpOhlc.SetInputValue(2, int((date.replace("-",""))))                
                # cpOhlc.SetInputValue(3, int((date.replace("-",""))))                
                # cpOhlc.SetInputValue(4, 1)                  # 요청 개수
                # cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5])    # 0:날짜, 2~5 OHLC
                # cpOhlc.SetInputValue(6, ord('D'))           # D: 일단위
                # cpOhlc.SetInputValue(9, ord('1'))           # 0: 무수정주가, 1:수정주가
                # cpOhlc.BlockRequest()
                # open = cpOhlc.GetDataValue(1, 0)
                # high = cpOhlc.GetDataValue(2, 0)
                # low = cpOhlc.GetDataValue(3, 0)
                # close = cpOhlc.GetDataValue(4, 0)
                # rows.append([date, code, name, buy, sell, qty, open, high, low, close])

        if not cpToday.Continue:
            break

    df = pd.DataFrame(rows, columns=columns)
    df.to_csv("C:/myData/STResult/result{}.csv".format(date))
    time.sleep(1000)
except Exception as ex:
    print(str(ex))
    os.system("pause")
