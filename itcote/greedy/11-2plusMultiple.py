s = input()
# s = '02984'

num = 0
for i in s:
    if int(i) in (0, 1) or num in (0, 1):
       num += int(i)
    else:
        num *= int(i)
print(num)