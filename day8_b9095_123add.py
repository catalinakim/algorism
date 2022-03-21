import sys
# n = int(sys.stdin.readline())

def numAdd(n):  # Not Solved -----------------
    count = 0
    sum = 0

    def dfs(n):
        print(n)
        nonlocal sum

        if sum > n:
            return

        if sum == n:
            nonlocal count
            count+=1
            print('+1')
            return

        # 4까지 반복문 돌면서
        for i in range(1, n):
            sum += i
            print('before call i:',i,'sum',sum)
            dfs(i+1)

    dfs(4)
    return count

print(numAdd(4))

