# https://www.acmicpc.net/problem/10773
n = int(input()) # 입력하는 숫자의 갯수
lst = []

for _ in range(n):
    num = int(input())
    if num != 0:  # 0이 아니면 그 숫자를 저장
        lst.append(num)
    else:  # 0이 나오면, 마지막에 저장한 숫자를 빼주기
        lst.pop()

print(sum(lst))