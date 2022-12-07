# 그리드 a, b, c 상화좌우 연결되는 경우

grid = ["??b", "abc", "cc?"]    # 2
# grid = ["abcabcab","????????"]  # 0
# grid = ["aa?"]  # 3

def solution(grid):
    answer = -1
    lenY = len(grid)
    lenX = len(grid[0])
    grid2 = grid.copy()

    # 재귀
    def dfs(x, y):
        pass
    #     종료조건
    #     if x<0 or x>=lenX or y<0 or y>= lenY:
    #         return
    #     반복실행
    # def check(x, y):


    # for i in grid:
    #     for j in i:
    for i in range(lenX):
        for j in range(lenY):
            if grid2[i][j] =='?':
                for k in ['a','b','c']:
                    grid2[i][j] = k
                    dfs()


    return answer

# print(grid[0][2])
print(solution(grid))

# dfs_bfs

# 비슷유형: https://www.acmicpc.net/problem/14502