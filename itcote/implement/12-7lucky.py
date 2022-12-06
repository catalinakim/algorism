# n = int(input())
# n = 123456
n = 123402

le = len(str(n))

# 1. 자리수를 구하고, 자리수의 반절로 앞의 숫자, 뒤의 숫자
le = le//2

front = n//10**le
back = n%10**le

# fSum = sum(str(front))  #문자열 sum불가

# 1-1.숫자의 각 자리수 합계
fSum = 0
bSum = 0
# 1-1-1. for문
# fList = list(front)  #'int' object is not iterable
fSList = list(str(front))
for i in fSList:
    fSum += int(i)
for i in list(str(back)):
    bSum += int(i)

# 1-1-2. 숫자를 리스트로 만들기 - 1.map, 2.for한줄
# fSum = sum(list(front))  #'int' object is not iterable
# 1-1-2-1. map
fList = list(map(int, str(front)))
fSum = sum(fList)
bSum = sum(list(map(int, str(back))))
# 1-1-2-2. for한줄
fList = [int(i) for i in str(front)]
print(fList)
# 1-1-2-3. eval 문자열 식의 계산결과값
fSum = eval("+".join(str(front)))
bSum = eval("+".join(str(back)))
print("eval fSum:", fSum)

if fSum == bSum:
    print("LUCKY")
else:
    print("READY")

# 2. 리스트로 만들고 slice
# lst = list(n)  # 'int' is not iterable
# lst = list(str(n))
lst = list(map(int, str(n)))
print(lst)
print(lst[:le])
print(lst[le:])
result = "LUCKY" if sum(lst[:le]) == sum(lst[le:]) else "READY"
print(result)