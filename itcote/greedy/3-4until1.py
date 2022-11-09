n, k = map(int, input().split())
cnt = 0

while True:
    if n%k == 0:
        n = n//k
        cnt += 1
    else:
        cnt += 1  #n%k
        n -= 1  #n%k
    if n == 1:
        break

print(cnt)