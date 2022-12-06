pos = input()

colStr = pos[0]
colNo = ord(colStr) - ord('a')
rowNo = int(pos[1]) - 1
xy = (rowNo, colNo)
print(xy)

dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]
lst = []
for i in range(8):
    x = xy[0]
    y = xy[1]
    lst.append((x + dx[i], y + dy[i] ))
print(lst)
cnt = 0
for x, y in lst:
    if 0 <= x <= 7 and 0<= y <= 7:
        cnt += 1
print(cnt)