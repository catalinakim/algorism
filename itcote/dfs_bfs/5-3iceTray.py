n, m = map(int, input().split())
# n, m = 3, 3
# n, m = 4, 5
'''
001
010
101
00110
00011
11111
00000
'''
graph = []
for i in range(n):
    row = list(map(int, input()))
    graph.append(row)
# print(graph)

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)


