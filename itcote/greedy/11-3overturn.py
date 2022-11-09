# s = input()
s = '101001001'
cnt = 0  #처음원소부터 끝까지 가면서 바뀐 횟수
cur = s[0]
for i in s[1:]:
    if cur != i:
        cnt += 1
        cur = i
print('cnt:', cnt)
# print(cnt/2)
# result = round(cnt/2)  # 반올림 앞자리가 홀수면 올림, 짝수면 내림
result = cnt//2 if cnt%2 == 0 else cnt//2 + 1
print(result)

# other's 숏코딩
# s=input().count
s = s.count
cnt2 = s('10') + s('01')  # 바뀐횟수
print('cnt2:', cnt2)
print((cnt+1)//2)  # 반올림

# https://www.acmicpc.net/source/38443431