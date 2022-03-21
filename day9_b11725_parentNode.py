import sys
sys.setrecursionlimit(10**9)

def dfs(V):
    visited[V]=True
    for i in graph[V]:
        if not visited[i]:
            answer[i]=V
            dfs(i)

N=int(input())

# 7인데 왜 8칸???
graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
answer=[1 for _ in range(N+1)]

# 트리를 그래프 형태로 생성
# 그 방식은 같은 이차원 배열을 사용하지만 그래프의 연결 상태만 표시해준다면 메모리의 사용을 크게 줄일 수 있다.
# 연결 상태만 표시하는 새로운 방식!
for i in range(N-1):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

#↓방문 순서를 확인할 필요없고 부모 노드만 확인하면 되기때문에 생략해도 상관x
for i in graph:
    i.sort()

dfs(1)

for i in range(2,len(answer)):
    print(answer[i])