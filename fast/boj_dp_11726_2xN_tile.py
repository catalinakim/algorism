# https://www.acmicpc.net/problem/11726
# 2×n 타일링 - 런타임 에러(index error) 해결
def dp(n):
    lst = [0 for index in range(n+1)]
    # if n == 1:
    lst[1] = 1
    # elif n == 2:

    # n = 1일때 index error
    # lst[2] = 2
    if n >= 2:
        lst[2] = 2
    # else:
    for i in range(3, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[n]

num = int(input())
print(dp(num) % 10007)
