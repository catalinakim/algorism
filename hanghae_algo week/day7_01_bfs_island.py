from collections import deque
from pprint import pprint

def island_bfs(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0]) # 행의 갯수, 열의 갯수
    cnt = 0 # 섬의 갯수

    for row in range(rows): # 오른쪽 하단까지 모든 점을 방문할껀데
        for col in range(cols):
            if grid[row][col] != '1': # 섬이 아니라면 넘어가고
                continue

            cnt += 1 # 방문을 시작했으면(bfs를 돌기 시작했으면) 섬 갯수 +1
            q = deque([(row, col)]) # 탐색 시작하는 점을 큐에 넣어

            while q: # 큐가 비어있을 때까지 bfs방문 계속
                x, y = q.popleft() # 제일 앞에 있는 점을 꺼내
                for i in range(4): # 4방향으로 돌면서 신규 좌표를 계산
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 그 신규 좌표가 섬이 아니거나 범위를 벗어났으면
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    # 섬이면 방문표시를 하고, 큐에 넣어줘
                    grid[nx][ny] = '0'
                    q.append((nx, ny))
    return cnt

def myIsland(grid):
    queue = deque() # 큐
    count = 0
    # visited = [[False] * len(grid[0])] * len(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print('in 2중 for i:',i,',j:',j)
            if grid[i][j] != '1':
                continue
            queue.append([i,j])
            # 여기서 방문처리를 하면 아래 if문에 계속 들어감, 어차피 이 코드가 실행된다는 건 [0][0]이 1이라는 뜻
            # 수정한 코드에서는 상관없네?
            grid[i][j] = '0'

            # 큐에 있는 좌표에서 상하우좌
            xmove = [-1,+1, 0, 0]
            ymove = [ 0, 0,+1,-1]
            while queue:
                nowX, nowY = queue.popleft()
                # print('nowX:',nowX,'nowY:',nowY)
                for i in range(4):
                    x = nowX + xmove[i]
                    y = nowY + ymove[i]
                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                        # print('x:',x,'y:',y,'-> if continue')
                        continue
                    elif grid[x][y] == '1':
                        # print('x:',x,'y:',y,'-> elif')
                        grid[x][y] = '0'
                        queue.append([x,y])
                    # print(queue)
                # print('---')  # end of for
            count += 1
    # print('count:',count)
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

'''
assert island_bfs(grid=[  # 함수결과가 1이 아니면 AssertionError
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_bfs(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3 '''
queue = deque()
queue.append([1,2])
lst = [['a','b','c'],['d','e','f']]
# print(lst[queue.pop()]) # list indices must be integers or slices, not list
x, y = queue.pop()
# print(lst[x][y]) # f