import sys  # not solved
# 다익스트라, 중복방문 허용x
# 최장거리를 모든 노드에 대해 구했을때, 최장거리가 몇개가 있는지
def near_naive(graph, start):
    N = len(graph)
    print(N)


with open("input.txt") as f:
    n, m = f.readline().split()
    # print(n, m)
    n, m = int(n), int(m)

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        # input = f.readline().split()
        # print(input)  # ['3', '6']
        a, b = map(int, f.readline().split())
        graph[a].append((a, b, 1))

print(graph, len(graph))
re = near_naive(graph, 1)
print(re)


# 파일을 open하면 무조건 close를 해야한다.
# 하지만 with문을 사용하면 close를 하지 않아도
# with블록이 끝나면 자동으로 close를 해주어 편리하게 사용할 수 있다.

# 패캠
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):
    print({x: 'zz' for x in graph})
    distances = {node: float('inf') for node in graph}
    print(distances)
    distances[start] = 0
    print(distances)
dijkstra(mygraph, 'A')

'''
>>> positive = float("inf")          # 양의 무한대
>>> print(positive)
inf

>>> negative = float("-inf")         # 음의 무한대
>>> print(negative)
-inf

>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}   # dict for는 key만 출력
>>> for i in x:
        print(i, end=' ')
a b c d

for 키, 값 in 딕셔너리.items():
     반복할 코드
'''