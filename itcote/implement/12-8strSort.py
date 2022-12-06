st = input()
stList = []
sumN = 0
hasDisit = False
for s in st:
    if s.isalpha():
        stList.append(s)
    elif s.isdigit():
        sumN += int(s)
        hasDisit = True
    else:
        print('not both')
stList.sort()
# stList.append(sumN)  -> join시: expected str instance, int found
print(stList)

# T.숫자가 없는 경우~!
result = ''
if hasDisit:
    result = ''.join(stList) + str(sumN)
else:
    result = ''.join(stList)
print(result)

# K1KA5CB7



# 숫자여부: https://codechacha.com/ko/python-isdigit/