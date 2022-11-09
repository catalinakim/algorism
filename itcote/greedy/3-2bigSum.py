# n, m, k = map(int, input().split())
# lst = list(map(int, input().split()))
n, m, k = 5, 6, 3
lst = [2, 4, 5, 4, 6]
lst.sort(reverse=True)

# v1. incomplete
# no = 0
# if m%k == 0:
#     no = lst[0] * k * (m//k-1) + lst[1] * k
#     print('if')
# else:
#     no = lst[0] * k * (m//k) + lst[1] * (m%k)
# print(no)

# 2번째 큰수는 1번씩만 더해야
total = 0
cnt = 0
while cnt < m:
    if m-cnt >= k:
        for _ in range(k):
            total += lst[0]
            cnt += 1
        if m-cnt > 0:
            total += lst[1]
            cnt += 1
    else:
        for _ in range(m-cnt):
            total += lst[0]
            cnt += 1
print(total)

# 수식
firstEa = m//(k+1) * k + m%(k+1)
total = lst[0] * firstEa + lst[1] * (m-firstEa)
print(total)
