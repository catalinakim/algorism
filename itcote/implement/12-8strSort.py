st = input()
stList = []
sumN = 0
for s in st:
    if s.isalpha():
        stList.append(s)
    elif s.isdigit():
        sumN += int(s)
    else:
        print('not both')
stList.sort()
# stList.append(sumN)  -> join시: expected str instance, int found
print(stList)

print(''.join(stList) + str(sumN))

# K1KA5CB7



# 숫자여부: https://codechacha.com/ko/python-isdigit/