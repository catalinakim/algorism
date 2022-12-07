from collections import deque

# 여러개 변수 선언 test
a, b = 10, 10
b += 10
print(a, b)

c = d = 0
d += 5
print(c, d)

# split(): 공백을 기준으로 분리
# n = input().split()  # 1 a d
# print(n)  # ['1', 'a', 'd']

# m = input().split('/')
# print(m)

e, f = map(int, ['121', '2323'])
print(e, f)

x, y = [2, 3]
print(x, y)

q = deque([[0, 0], [1, 2]])
i, j = q.popleft()
print(i, j)
