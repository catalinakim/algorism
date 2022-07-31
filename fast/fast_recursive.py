def multiple(num):
    # if num == 1:
    #     return 1
    if num <= 1:
        return num
    result = num * multiple(num-1)
    return result

def multiple2(num):
    if num >= 1:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result
    return num

def listSum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def listSumRec(lst):
    if len(lst) == 1:
        return lst[0]
    num = lst.pop()  # but 리스트 요소를 1개빼고 삭제를 해버리네 ㅋㅋ -> 리스트를 복사해서 쓰면 될듯 ㅋㅋ
    return num + listSumRec(lst)

print(multiple(3))
print(multiple(1))
print(multiple(0))
print(multiple2(3))
print(multiple2(1))
print(multiple2(0))

lst = [1,3,6,7,10]
print(listSum(lst))
print(listSumRec(lst))
print(lst)