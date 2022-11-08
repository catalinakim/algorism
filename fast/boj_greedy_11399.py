# https://www.acmicpc.net/problem/11399
# ATM

n = int(input())
lst = list(map(int, input().split()))

n = 5
lst = [3,1,4,3,2]
lst.sort()
print(lst)

time = 0
for i in range(n):
    time += sum(lst[:i+1])

print(time)