# n = int(input()) --------- ing

# for i in range(n):
# str = input()

str = '(())())'

stack = []

for i in range(len(str)):
    print(i)
    if str[i] == '(':
        stack.append(str[i])
        print(stack)
    else:
        if len(stack) > 0:
            stack.pop()
            print(stack)
if len(stack) == 0:
    print('YES')
else:
    print('NO')


