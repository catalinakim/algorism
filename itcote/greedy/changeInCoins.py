# 예제3-1 거스름돈(p87)
# 백준 5585

price = int(input())
n = 1000 - price

coins = (500, 100, 50, 10, 5, 1)
ea = 0

for coin in coins:
    ea += n // coin  #몫은 갯수에 더하기
    n = n % coin     #위 동전에서 바꾸고 남은 잔돈은 다시 금액에 저장
    if n == 0:
        break

print(ea)







