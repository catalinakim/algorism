# https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open("../input.txt", "r")
from guppy import hpy  # https://rateye.tistory.com/1649
h = hpy()

com = int(sys.stdin.readline())
line = int(sys.stdin.readline())
dct = {}

for i in range(1, com+1): # KeyError방지위해 미리 key입력
    dct[i] = []

for i in range(line):
    # print(i, dct)
    node, adj = map(int, sys.stdin.readline().split())
    if node in dct.keys():
        dct[node].extend([adj])
        dct[adj].extend([node])  # 양방향 -> 무한루프..
        # KeyError: 5
    else:
        dct[node] = [adj]
    # 양방향 -> 아래 while문에서 무한루프 돌음....
    # if adj in dct.keys():
    #     dct[adj].extend([node])
    # else:
    #     dct[adj] = [node]
# print(dct)

visited = []
need_visit = [1]
count = 0
while need_visit:
    cur = need_visit.pop()
    if cur not in visited:
        visited.append(cur)
        # 수정본
        need_visit.extend(dct[cur])
    count += 1
    # print(count)
    # print('cur',cur)
    # print('visited',visited)
    # if cur in dct.keys():
    #     print('if')
    #     need_visit.extend(dct[cur]) # KeyError: 6
    # else:
    #     continue
    # print('need_visit',need_visit)
    # if count == 10:
    #     exit()
print(len(visited)-1)
# print(h.heap())

# 메모리 초과
# 리스트 부분을 짤라 쓸때마다 메모리를 잡아먹어요.
# 전 리스트를 자르지 않고, 시작과 끝 인댁스를 써서 해결했어요.

# 이미 체크한 곳인지 혹은 방문한 곳인지 확인하여
# 중복으로 q 에 넣는 경우를 피해야 할 것 같습니다.

'''
7
4
1 2
2 4
4 3
3 5

# 반례 답 3인데 1나옴
4
3
1 4
2 4
2 3
'''

# bfs, dfs 방식 풀이 : https://chancoding.tistory.com/60