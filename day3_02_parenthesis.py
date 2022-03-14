def is_valid_parenthesis(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:              # 닫는 녀석이 나오면 stack의 top이랑 무조건 같아야 하는데
            if not stack:  # 닫는 애가 나왔는데 stack이 비었으면
                return False

            top = stack.pop()      # 제일 위에 있는 애를 꺼내
            if pair[char] != top:  # 닫는 녀석의 짝과 top이 같으면(진행), 같지 않으면 false
                return False

    # [[{{}} -> for문 돌고 [[ 만 남았을때, 비었는지 체크
    # stack 배열이 비어있으면(stach이 False이면) True 출력
    # stack 배열에 값이 있으면(stach이 True이면) False 출력
    return not stack

assert is_valid_parenthesis("()")
assert is_valid_parenthesis("()[]{}")  # 유효하지 않은 괄호 넣으면, AssertionError 에러 발생
assert not is_valid_parenthesis("(]")

print(bool([]))     # []은 false
print([] is False)  # 근데 이건 아니라네..
print(not [])       # not 0 = True
print(not [12])     # not 1(higher value) = False

# return not ANY_RESULT 의 의미는
# return False if ANY_RESULT else True

# 사실 파이썬은 []를 스택으로 사용하면 됨, but 다른 언어 사용할 경우
