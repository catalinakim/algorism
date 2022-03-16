n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
for i in lst2:
   if i in lst1:
       print(1)
   else:
       print(0)


# set 시간 차이???