# https://www.acmicpc.net/problem/1904
# 01 타일
# 00과 1만으로

n = int(input())

lst = [0 for idx in range(n+1)]

lst[1] = 1
if n >= 2:
    lst[2] = 2

for i in range(3, n+1):
    lst[i] = (lst[i-1] + lst[i-2]) % 15746

# print(lst[n] % 15746) # 메모리초과 MemoryError
print(lst[n])

import sys
# print(sys.maxsize) # 9223372036854775807