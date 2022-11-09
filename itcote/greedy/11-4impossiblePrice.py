from itertools import combinations
n = 5
lst = [3,2,1,1,9]
n = 3
lst = [3, 5, 7]

result = 0
sumList = []
if min(lst) > 1:
    result = 1
else:
    for i in range(1, n+1):
        combiList = list(combinations(lst, i))
        sumList.extend(list(map(sum, combiList)))
        print(sumList)
    sumList = list(set(sumList))
    print(sumList)
    for i in range(1, len(sumList)):
        if i not in sumList:
            result = i
            break
print(result)

