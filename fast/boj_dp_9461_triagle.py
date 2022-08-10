# 파도반 수열 https://www.acmicpc.net/problem/9461
# 첫 삼각형의 변의 길이는 1

n = int(input())
lst = [0] * 101
lst[1] = 1
lst[2] = 1
lst[3] = 1
lst[4] = 2
lst[5] = 2
for i in range(6, 101):
    lst[i] = lst[i-1] + lst[i-5]

for _ in range(n):
    num = int(input())
    # if num > 5:
    #     for i in range()
    print(lst[num])