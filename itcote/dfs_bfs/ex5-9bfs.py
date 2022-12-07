from collections import deque

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],    # 5
  [7],
  [2, 6, 8], # 7
  [1, 7]
]

def bfs(graph, v, visited):
  queue = deque()
  queue.append(v)
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    # queue.append(graph[v])  #리스트[2, 3, 8]가 큐에 들어감
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * len(graph)  # [False, False,

bfs(graph, 1, visited)