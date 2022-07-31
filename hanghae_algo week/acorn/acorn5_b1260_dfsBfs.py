# https://www.acmicpc.net/problem/1260
# 입력으로 주어지는 간선은 양방향이다.

import sys
from pprint import pprint
sys.stdin = open("../input.txt", "r")
ver, edge, start = map(int, input().split())
dct = {}
for i in range(1, ver+1): # KeyError방지위해 미리 key입력
    dct[i] = []

for i in range(edge):
    node, adj = map(int, input().split())
    if node in dct.keys():
        dct[node].extend([adj])
        dct[adj].extend([node])  # 양방향
    else:
        dct[node] = [adj]
print(dct)
def dfs():
    visited = []
    need_visit = []
    need_visit.append(start)
    while need_visit:
        cur = need_visit.pop()
        if cur not in visited:
            visited.append(cur)
            if len(dct[cur]) > 0:
                need_visit.extend(sorted(dct[cur], reverse=True))
                # 'NoneType' object is not iterable
                # 0초과인 경우만 했는데도, 같은 에러네..
                # 아 lst.sorted는 반환안하지...
            # KeyError: 4 사전에 없는 key에 접근하게 되면 KeyError 가 발생
            #: https://korbillgates.tistory.com/95
    return visited

def bfs():
    visited = []
    need_visit = []
    need_visit.append(start)
    while need_visit:
        cur = need_visit.pop(0)
        if cur not in visited:
            visited.append(cur)
            need_visit.extend(sorted(dct[cur]))
    return visited

print(*dfs())
print(*bfs())

# 예제 1번만 맞고, 2,3번은 틀림
# 기존 코드는 예제2에서 인접노드 정보에 5번에 없어서 5번노드를 가지 않네

'''반례 
입력
4 3 1
1 2
1 4
2 3
출력
1 2 3 
1 2 4 3
추가반례 : https://www.acmicpc.net/board/view/86724
입력으로 주어지는 간선은 양방향입니다. 따라서 A노드에서 B노드로 갈 수 있다면 B노드에서 A노드로도 갈 수 있습니다.
작성하신 코드는 한 쪽 방향만 고려하고 있기 때문에 오답이 출력됩니다.
'''

sys.stdin.close()