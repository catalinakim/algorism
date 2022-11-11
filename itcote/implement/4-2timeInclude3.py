n = int(input())

#시간에 3이 포함된 갯수 - 3시, 13시, 23시
hourUsing3 = 0

if n < 3:
    hourUsing3 = 0
elif n < 13:
    hourUsing3 = 1
elif n < 23:
    hourUsing3 = 2
else:
    hourUsing3 = 3

sum = hourUsing3 * 60 * 60

#그 외 시간일때 분, 초에 3이 포함된 경우
restOfHour = n + 1 - hourUsing3  # 0시 포함으로 +1

# 0~60분에 3이 포함된 경우: 3, 13, 23, 30, 31 ~ 39, 43, 53 = 15
# restOfHour * (15 * 60 * (분에 포함, 초에 포함) - 분&초에 둘다있는경우 중복계산 제거)
sum += restOfHour * (15 * 60 * 2 - 15 * 15)

print(sum)
