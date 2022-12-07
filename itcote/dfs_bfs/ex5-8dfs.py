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
visited = [False] * len(graph)
def dfs(graph, v, visited):
    #방문처리
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        # if visited[i] == False:
        if not visited[i]:  # False면
            dfs(graph, i, visited)

dfs(graph, 1, visited)
