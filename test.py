import pyupbit

access = "5ZBBptgIVeD2DC9xeXg1ukqONuCf7IdKOrUl2Qnc"          # 본인 값으로 변경
secret = "Q4TsO6C8WLiSNoBpSOVobbxxkBtI7WA6W4NVsGgW"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회