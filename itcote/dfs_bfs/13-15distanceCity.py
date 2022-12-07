# https://www.acmicpc.net/problem/18352
from collections import deque
'''
1 2
1 3
2 3
2 4

4 4 1 1
1 2
1 3
2 3
2 4
'''
n, m, k, x = map(int, input().split())
# n, m, k, x = 4, 4, 2, 1
graph = {}
for i in range(m):
    start, des = map(int, input().split())
    if start in graph:
        graph[start].append(des)
    else:
        graph[start] = [des]
# print(graph)

visited = [False] * (n+1)
distance = [999999] * (n+1)

def bfs(city):
    queue = deque([city])
    visited[city] = True
    distance[city] = 0
    while queue:
        v = queue.popleft()
        visited[v] = True
        if v in graph:
            for i in graph[v]:
                print('v:',v,', i:', i)
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    distance[i] = distance[v] + 1
                # if distance[i] > distance[v] + 1:
                #     distance[i] = distance[v] + 1
                print('거리:', distance)

        # print('queue', *queue)
bfs(x)
# distance리스트에 거리가 k인 도시번호들 ->한줄에 하나씩 출력, 없으면 -1
# if k in distance:
found = False
for i in range(1, len(distance)):
    if distance[i] == k:
        print(i)
        found = True
if not found:
    print(-1)

