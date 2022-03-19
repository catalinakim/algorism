def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]  # 엄밀히 말하면 x,y 바껴야
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])  # 행, 열(세로,기둥) 갯수
    cnt = 0

    for row in range(rows):  # 2중 for문
        for col in range(cols):
            if grid[row][col] != '1':  # 1이 아니면 지나가
                continue

            # 섬 하나를 0으로 바꾸는 코드[시작]
            cnt += 1  # 1이라면 섬 갯수 +1
            stack = [(row, col)]  # 좌표를 스택에 넣기

            while stack:  # 스택에 방문할 곳이 남아있는 동안
                x, y = stack.pop()  # 스택에서 가장 위에 있는 좌표를 꺼내
                grid[x][y] = '0'  # 0으로 변경
                # 상하좌우(4번 반복)
                for i in range(4):  # i가 0~3
                    nx = x + dx[i]  # newX 우,좌,하,상
                    ny = y + dy[i]
                    # x가 0보다 작거나, 행의 갯수와 같거나 넘어가거나 = x, y가 범위를 넘어가거나 1이 아니어서 방문할 가치가 없을 때는 stack에 넣지 않아
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
            # 섬 하나를 0으로 바꾸는 코드[종료]

    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
''' 
상하좌우 dfs로 들어가
[0,0] 들어가서 1이면 1->0으로 바꾸고, 상하좌우로 방문
상하좌우가 다 0으로 바껴서 주위가 0이면 탐색 끝, 섬 갯수 +1
또 쭉 가다가 1 발견하면 스택에 넣어
'''
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3