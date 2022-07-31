# https://www.acmicpc.net/problem/20291

n = int(input())
dct = {}
count = 0
for i in range(n):
    name, extension = input().split('.')
    if extension in dct.keys():
        dct[extension] += 1
    else:
        dct[extension] = 1

# print(dct)

lst = sorted(dct.keys())
# print(lst)

for extension in lst:
    print(extension, dct[extension])