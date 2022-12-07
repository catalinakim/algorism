from collections import deque
from pprint import pprint
n, m = map(int, input().split())
lst = []

for i in range(n):
    lst.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([(0, 0)])
cnt = 0
while queue:
    x, y = queue.popleft()  #cannot unpack non-iterable int object
    print(x, y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if lst[nx][ny] == 0:
            continue
        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if lst[nx][ny] == 1:
            lst[nx][ny] = lst[x][y] + 1
            queue.append((nx, ny))
    cnt += 1
    if cnt == 100:
        break
    print(*queue)
pprint(lst)
print(lst[n-1][m-1])
'''
5 6
101010
111111
000001
111111
111111
'''

from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

