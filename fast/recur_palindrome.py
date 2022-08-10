# 재귀 13.2 - 플랜드롬

def recur(s):
    # isP = True # 리팩토링하면, 각 조건문에서 return해서 필요하지 않음
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        # isP = recur(s[1:-1])
        # return isP
        # 선생님
        return recur(s[1:-1])
    else:
        # isP = False
        # 리팩토링1
        return False

    # if isP == False:
    #     return False
    # return isP

print(recur('level'))
print(recur('leel'))
print(recur('levep'))
print(recur('leveew'))
