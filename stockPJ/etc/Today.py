import sys, ctypes
import win32com.client
import pandas as pd
from datetime import datetime
from slacker import Slacker
import time
from urllib.request import urlopen
import csv
import os
date = "2020-12-21"
# date = datetime.today().strftime('%Y-%m-%d')

cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')  # 종목코드
cpStatus  = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')  # 주문관련
cpStock = win32com.client.Dispatch("DsCbo1.StockMst")
cpOhlc = win32com.client.Dispatch("CpSysDib.StockChart")
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')    # 계좌 정보
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')   # 주문 가능 금액
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 
cpToday = win32com.client.Dispatch('CpTrade.CpTd5341')      # 금일 주문내역
cpTodayPL = win32com.client.Dispatch('CpTrade.CpTd5342')    # 금일 체결기준 내역

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

    # 금일 주문내역 받아오기
    cpToday.SetInputValue(0, acc)           # 계좌번호
    cpToday.SetInputValue(1, accFlag[0])    # 상품관리구분코드
    cpToday.SetInputValue(4, 0)             # 순차정렬
    cpToday.SetInputValue(5, 20)            # 요청개수

    columns = ['DATE', 'CODE', 'NAME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'BUY', 'SELL', 'QTY']
    rows = []
    while True:
        cpToday.BlockRequest()
        print(cpToday.GetHeaderValue(6))
        count = cpToday.GetHeaderValue(6) # 수신 개수
        # columns = ['DATE', 'CODE', 'NAME', 'OPEN','HIGH', 'LOW', 'CLOSE','BUY', 'SELL', 'QTY', 'PL', 'ROI' ]
        for i in range(count):
            if cpToday.GetDataValue(9, i) > 0:      # 
                code = cpToday.GetDataValue(3, i)   # 종목코드
                name = cpToday.GetDataValue(4, i)   # 종목명
                buy = 0
                sell = 0
                if cpToday.GetDataValue(35, i) == '2': # 매수일때
                    buy = cpToday.GetDataValue(11, i)  # 매수단가
                else:                                  # 매도일때
                    sell = cpToday.GetDataValue(11, i) # 매도단가
                qty = cpToday.GetDataValue(10, i)  #체결수량
                # print(date, code, name, buy, sell, qty)

                cpOhlc.SetInputValue(0, code)               # 종목코드
                cpOhlc.SetInputValue(1, ord('2'))           # 1:기간, 2:개수
                cpOhlc.SetInputValue(2, int((date.replace("-",""))))                
                cpOhlc.SetInputValue(3, int((date.replace("-",""))))                
                cpOhlc.SetInputValue(4, 1)                  # 요청 개수
                cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5])    # 0:날짜, 2~5 OHLC
                cpOhlc.SetInputValue(6, ord('D'))           # D: 일단위
                cpOhlc.SetInputValue(9, ord('1'))           # 0: 무수정주가, 1:수정주가
                cpOhlc.BlockRequest()
                open = cpOhlc.GetDataValue(1, 0)
                high = cpOhlc.GetDataValue(2, 0)
                low = cpOhlc.GetDataValue(3, 0)
                close = cpOhlc.GetDataValue(4, 0)

                rows.append([date, code, name, open, high, low, close, buy, sell, qty])

        if not cpToday.Continue:
            break

    cpTodayPL.SetInputValue(0, acc)           # 계좌번호
    cpTodayPL.SetInputValue(1, accFlag[0])    # 상품관리구분코드
    cpTodayPL.SetInputValue(2, 20)            # 요청개수
    cpTodayPL.SetInputValue(3, "1")           # 요청일 구분코드 "1":금일 "2":전일(default)

    columns2 = ['CODE','TYPE','PL']
    rows2 = []
    while True:
        cpTodayPL.BlockRequest()
        print(cpTodayPL.GetHeaderValue(8))
        count = cpTodayPL.GetHeaderValue(8)   # 수신개수
        medo = cpTodayPL.GetHeaderValue(9)    # 매도정산금합
        mesu = cpTodayPL.GetHeaderValue(10)   # 매수정산금합

        for i in range(count):
            if cpTodayPL.GetDataValue(3, i) > 0:        # 체결수량
                code = cpTodayPL.GetDataValue(0, i)     # 종목코드  
                type = cpTodayPL.GetDataValue(10, i)    # 매매구분 "매도", "매수"
                pl = cpTodayPL.GetDataValue(24, i)      # 정산금액
                rows2.append([code, type, pl])
        if not cpTodayPL.Continue:
            break        
    df = pd.DataFrame(rows, columns=columns)
    df.to_csv("C:/myData/TodayResult/res{}.csv".format(date))
    df2 = pd.DataFrame(rows2, columns=columns2)
    df2.to_csv("C:/myData/TodayResult/pls{}.csv".format(date))
    print("UPDATE FINISHED")
    time.sleep(10)
except Exception as ex:
    print(str(ex))
    os.system("pause")
