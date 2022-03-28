from collections import deque
''' 예제2 답:8
10 3
2 9 5
'''
# N, M = map(int, input().split())
N, M = 10, 3
# lst = list(map(int, input().split()))
lst = [2, 9, 5]

# print(list(range(1,N+1)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(i for i in range(1, N+1)))  # 상동

que = deque(list(range(1,N+1)))

def left(que):
    que.append(que.popleft())


for l in lst:
    idx = que.index(l)
    print(idx+1)
    # while que.popleft() == l:
    #     pass

# left(que)
for i in que:
    print(i, end=' ')
