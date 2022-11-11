n = int(input())
# go = list(input().split())
go = ['R', 'R', 'R', 'U', 'D', 'D']

# print(go)

s = [0, 0]
dir = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for g in go:
    i = dir.index(g)
    print('g:', g, ',i:', i)
    if 0 <= s[0]+dx[i] <= n-1 and 0 <= s[1]+dy[i] <= n-1:
        s[0] += dx[i]
        s[1] += dy[i]
s[0] += 1
s[1] += 1

print(s)
print(*s)
