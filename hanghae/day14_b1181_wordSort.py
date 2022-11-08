# https://www.acmicpc.net/problem/1181
import sys
n = int(sys.stdin.readline())
# n = int(input())

lst = []
for i in range(n):

    # sys.stdin.readline()은 한줄 단위로 입력, 개행문자가 같이 저장됨
    # 만약 3을 입력했다면, 3\n 이 저장
    # word = sys.stdin.readline()   # im\n 저장됨

    # word = input()
    word = sys.stdin.readline().strip()
    if word not in lst:
        lst.append(word)
lstSorted = sorted(lst, key = lambda x:(len(x), x))
# print(lst)
# print(lstSorted)
for i in lstSorted:
    print(i)
