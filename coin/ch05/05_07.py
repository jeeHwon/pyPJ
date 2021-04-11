import pybithumb

df = pybithumb.get_ohlcv("BTC")
ma5 = df['close'].rolling(window=5).mean()
last_ma5 = ma5[-2]

price = pybithumb.get_current_price("BTC")

if price > last_ma5:
    print("상승장")
else:
    print("하락장")

print(ma5)
print(ma5[0])
print(ma5[1])
print(ma5[2])
print(ma5[-2])  # 전날 5이평
