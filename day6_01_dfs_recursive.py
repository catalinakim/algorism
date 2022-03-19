def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c): # 좌표
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(m):
        for c in range(n):
            node = grid[r][c]
            if node != '1':
                continue
            # 새 섬 발견시 cnt + 1 (재귀가 다 돌고 돌아오면 섬 하나 끝)
            cnt += 1
            dfs_recursive(r, c)

    return cnt

def myIsland(grid): # 혼자안되서 위에 보고함
    count = 0

    def bfs(x, y):
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]=='0':
            return
        grid[x][y] = '0'  # 방문처리
        bfs(x+1,y)
        bfs(x-1,y)
        bfs(x,y+1)
        bfs(x,y-1)
        return

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '1':
                continue
            count += 1
            bfs(i,j)
    print(count)
    return count

var = myIsland(grid=[["1", "1", "1", "1", "0"],
                     ["1", "1", "0", "1", "0"],
                     ["1", "1", "0", "0", "0"],
                     ["0", "0", "0", "0", "0"]]) == 1
var2 = myIsland(grid=[["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"] ]) == 3
print(var)
print(var2)

assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

# 재귀 구구단
def multi_table_2(n):
    if n==0:
        print('end')
    else:
        multi_table_2(n-1)
        print('2 * {} = {}'.format(n,2*(n)))

# multi_table_2(10)

# 팩토리얼(factorial)
# 그 수보다 작거나 같은 모든 양의 정수의 곱
# n이 하나의 자연수일 때, 1에서 n까지의 모든 자연수의 곱을 n에 상대하여 이르는 말
def factorial(n):
    if n==1:
        print('n = 1, return 1')
        return 1
    else:
        # return n * factorial(n-1)
        print('n:',n)
        recur = factorial(n-1)
        print('재귀 후 :',n,'*', recur,'-> return',n*recur)
        return n * recur

# print(factorial(5))

# 리스트
lst = ['a','b','c','d']
# print(lst[1,2]) # 틀린 문법