# 13.2
# 정수 n
# n이 홀수이면 3*n + 1, 짝수이면 n을 2로 나누기, 과정을 모두 출력
def func(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 1:
        # n = n * 3 + 1
        # func(n)

        # 선생님 - 리팩토링
        func(n * 3 + 1)

    else:
        n = n // 2
        func(n)

func(3)
