# Auto Stock Trader
> 너도나도 주식 열풍일 때 주식 공부와 Python 공부의 목적으로 개발한 프로그램입니다. 

## 기능 요약
아래 링크를 클릭하시면 주요 기능을 살펴 보실 수 있습니다.
https://github.com/jeeHwon/pyPJ/blob/master/stockPJ/AutoStockTrader.pdf

## 프로그램 작동 영상
아래 링크를 클릭하시면 실제 자동 매매 프로그램이 동작하는 모습을 보실 수 있습니다.

## 주요내용
* 마감 후에 자동으로 당일 국내 주식 OHLC 정보를 DB에 저장하고 Keras Sequential 모델로 다음날 종가를 예측하여 최상위 기업을 리스트업 하는 기능을 구현하였습니다. 
* 추가로 볼린저 밴드 추세 추종 매매 기법 등의 매매 방식을 코드로 구현하여 모듈화했습니다. 
* Matplotlib를 활용해 데이터 시각화를 통해 데이터의 분석이 쉽게 하였습니다. 
* CREON API를 활용해 매일 아침 장 시작 전 로그인하여 전날 리스트업한 종목을 Slackbot이 알람으로 알려주고 장 시작 시 매수 포인트와 매도 포인트에서 자동으로 주식을 매매하도록 설계하였습니다. * 모든 프로세스가 Window 작업 스케줄러로 자동 실행되며, 진행 상황, 매수, 매도 결과 등을 SlackBot이 알려주면 사람은 확인만 하면 되는 방식으로 프로그램화하였습니다. 
* 실제 지금도 직접 사용하는 프로그램으로서 애정을 가지고 지속해서 코드를 업데이트 하고 있습니다. 소소하지만 수익률이 조금씩 상승하고 있습니다.
