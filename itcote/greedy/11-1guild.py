# n = int(input())
# lst = map(int, input().split())
n = 5
lst = [2,3,1,2,2]
lst = [3,3,5,5,5]  #1
lst = [1,2,3,4,5]
lst = [1,1,1,1,2]
lst = [4,3,4,4,4]
lst = [1,1,2,2,2]

lst.sort()
result = 0

# v1. incomplete
# for i in range(n):
# for i in range(len(lst)):
#     # i=0
#     print(lst)
#     print("i:", i, lst[i:i+lst[i]], " len:", len(lst[i:i+lst[i]]))
#     if max(lst[i:i+lst[i]]) == len(lst[i:i+lst[i]]):
#         print('ok')
#         result += 1
#         # lst = lst[lst[i]:]
#     elif max(lst[i:i+lst[i]]) > len(lst[i:i+lst[i]]):
#         break

num = 0  # 현재 그룹 인원
for i in lst:
    num += 1  # 일단 현재 참가자를 그룹에 집어넣어
    if num >= i:  # 그룹 인원이 공포도 이상이면
        result += 1  # 현재 그룹 마감해서 결과 +1
        num = 0  # 그룹 인원 초기화
print(result)