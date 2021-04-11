import pybithumb


detail = pybithumb.get_market_detail("BTC")
# print(detail)

orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook['bids']
asks = orderbook['asks']
# print(bids)
# print(asks)

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("매수호가: ", price, "매수잔량: ", quant)
