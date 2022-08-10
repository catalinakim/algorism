# 1,2,3,의 조합으로 N이 되는 경우의 수
def recur(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recur(n-1) + recur(n-2) + recur(n-3)

print(recur(3))
print(recur(4))
print(recur(5))
print(recur(6))
