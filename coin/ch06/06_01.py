import pyupbit

with open('C:\\myKey\\upbit.txt') as f:
    access = f.readline().strip()
    secret = f.readline().strip()

upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회