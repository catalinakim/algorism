import sys

n = int(sys.stdin.readline())

def myqueen(n):  # 시간초과
    count = 0
    visited = [-1]*n

    def check(row):
        for r in range(row):
            if visited[r] == visited[row] or row - r == abs(visited[row] - visited[r]):
                return False
        return True

    def dfs(row):
        if n == row: # if문 먼저(순서)
            nonlocal count
            count+=1

            return

        for col in range(n):
            visited[row] = col
            if check(row):
                dfs(row+1)
        return

    dfs(0)
    return count


# 시간초과 참고 : https://txegg.tistory.com/108
count = 0
visited = [-1]*n

def dfs(row, n):

    global count
    def check(row):
        for r in range(row):
            if visited[r] == visited[row] or row - r == abs(visited[row] - visited[r]):
                return False
        return True


    if n == row: # if문 먼저(순서)
        count+=1

        return

    for col in range(n):
        visited[row] = col
        if check(row):  # if문을 여기에?
            dfs(row+1,n)
    return

dfs(0,n)

print(count)