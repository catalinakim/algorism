n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

# print(lst)

a = []
for i in lst:
    a.append(min(i))
print(max(a))
