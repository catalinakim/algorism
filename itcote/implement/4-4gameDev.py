import copy
# n, m = map(int, input().split())
# x, y, d = map(int, input().split())

# mapList = []
# for i in range(n):
#     mapList.append(list(map(int, input().split())))
n, m = 4, 4
# x, y, d = 1, 1, 0
# mapList = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
x, y, d = 2, 2, 1
mapList = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]

# 0:북 1:동 2:남 3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ds = ['북','동','남','서']

visit = copy.deepcopy(mapList)
groundDct = {}
groundList = []
for i in range(n):
    for j in range(m):
        if mapList[i][j] == 0:
            # groundDct[(i, j)] = 0
            groundList.append([i, j])
visit[x][y] = 1
cnt = 1
eachCnt = 1  # -> visit에 누적?

while True:
    # 4면이 다 가봤거나 바다면, 뒤로 1칸, 뒤가 바다면 멈춤
    bx, by = 0, 0
    if eachCnt == 4:
        print(f'({x},{y}) 4면 모두 가봤거나 바다')
        back = d + 2 if d <= 1 else d - 2  # 뒷 방향으로(1<->3, 0<->2)
        bx, by = x + dx[back], y + dy[back]
        # 뒷 방향이 0이상 n-1이고, 육지면, 뒤로 1칸 이동 >> bx, by 범위

    else:
        # 왼쪽방향(반시계 90도)로 회전
        # d = (d % 4 + 3) % 4  # d = d - 1 인데 outOfIndex 방지용 식
        d = (d - 1 + 4) % 4    # 상동
        print(f'({x},{y}) {ds[d]}쪽({d})방향')
    nx, ny = x + dx[d], y + dy[d]

    if 0 <= nx <= n-1 and 0 <= ny <= n-1:
        if eachCnt == 4 and mapList[bx][by] == 0:
            print(f'-> 4면 다 가봤거나 바다이고, 뒤({bx},{by})가 육지여서, 뒤로 1칸 이동')  # >> 1단계로, eachCnt를 visit처럼 좌표별 저장
            x, y = bx, by
        elif eachCnt == 4 and mapList[bx][by] == 1:
            print('-> 4면 다 가봤거나 바다이고, 뒤쪽이 바다여서 멈츰')
            break

        # 육지인데 가보지 않은 곳이면 1칸 Go
        elif mapList[nx][ny] == 0 and visit[nx][ny] == 0:  # visit만 해도될듯
            print('-> go to', ds[d], f'({nx},{ny})')
            x, y = nx, ny
            visit[x][y] = 1  # 방문처리
            cnt += 1
            eachCnt = 0
        else: # 바다거나 가본 곳
            # d = (d - 1 + 4) % 4
            print('- sea or visited at', f'({nx},{ny})', 'in', ds[d])
            eachCnt += 1
    else: # 왼쪽방향이 갈수없는 외각이면, 다음방향으로
        continue

print('cnt', cnt)
