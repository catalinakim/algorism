import sys
sys.setrecursionlimit(10**9)  # 10의 9제곱 = 1,000,000,000 (10억)

N = int(input())  # 노드의 갯수

graph = [[] for _ in range(N+1)]      # 노드 연결 정보
#   0   1   2   3   4   5   6   7
# [[], [], [], [], [], [], [], []]
#       6                   1
#               6           3
#               5       3
#       4           1
#           4       2
#                   7           4
visited = [False for _ in range(N+1)] # 방문여부
#    0      1      2      3      4      5      6      7
# [False, False, False, False, False, False, False, False]
# [False, True, False, False, False, False, False, False] V=1
# [False, True, False, False, True, False, False, False]    4
# [False, True, True, False,  True, False, False, False]    2
# [False, True, True, False,  True, False, False, True]     7
# [False, True, True, False,  True, False,  True, True]     6
answer = [0 for _ in range(N+1)]      # 부모노드 저장

# 노드 연결 정보를 리스트에 저장
for i in range(N-1):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
print(graph)  # [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

# 작은 숫자 순서로 탐색하려면, 생략해도 상관x
for i in graph:
    i.sort()

#  0      1     2      3        4       5     6      7
# [[], [4, 6], [4], [5, 6], [1, 2, 7], [3], [1, 3], [4]]
# 부모에서 자식으로 이동하면서, answer[자식]에 부모값 저장
def dfs(V):                # V = 1                V=4                    V=2
    # 방문처리
    visited[V]=True        # visited[1]=True      visited[4]=True        visited[2]=True
    for i in graph[V]:     # [4, 6]               [1, 2, 7]              [4]
        # 방문안했으면 실행(이미 방문한 것은 부모노드)
        if not visited[i]: # visited[4]가 false면  1은 방문했고, 2는 False  <-
            answer[i]=V    # answer[4]=1          answer[2]=4
            dfs(i)         # dfs_bfs(4)               dfs_bfs(2)
#                                                 i = 7 방문안했어서
#                                                 answer[7]=4
#                                                 dfs_bfs(7)
#                                                 i = 4 방문했어서 <-
#                                              <- 7까지 다 돌아서
#                          i=6 방문안했어서 answer[6]=1넣고 dfs_bfs(6)                     for 끝나서 dfs_bfs 종료
#                           6 방문처리하고 [1, 3] 1은 방문했고, answer[3]=6 dfs_bfs(3)  for끝나서 --^
#                           3 방문처리하고 [5, 6] answer[5]=3 dfs_bfs(5)  6방문했어서 --^
#                           5 방문처리하고 [3] 3은 이미 방문했어서  ---^

dfs(1) # 루트 1부터 탐색 시작

for i in range(2,len(answer)): # range(2,8)
    print(answer[i])           # 2~7번 노드의 부모 출력