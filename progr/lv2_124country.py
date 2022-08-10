# https://school.programmers.co.kr/learn/courses/30/lessons/12899?language=python3

import math
# from IPython.display import display
from convert10toNnotation import convert
# from pandas import Series, DataFrame, set_option
import pandas as pd

# 다른사람 코드 - 3진법 변형(https://mingchin.tistory.com/76)
def solution_ref2(n):
    num = ['1','2','4']
    answer = ""
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    return answer
# print(solution_ref2(10))

def solution(n):
    # answer = 0
    # lst = [1,2,4]
    # 시도1 - x
    # if n > len(lst):
    #     quotient = n//len(lst)
    #     remainder = n%len(lst)
    #     answer = quotient*10 + lst[remainder-1]
    # else:
    #     answer = lst[n-1]
    # 시도2 - x
    # quotient = n / len(lst)
    # remainder = n % len(lst)
    # print('_몫:', quotient, ', 나머지:', remainder)
    # answer = math.ceil(quotient-1) * 10 + lst[remainder - 1]

    # 남의 코드1 (https://mingchin.tistory.com/76)
    # 3진법으로 표현하는데
    answer = ''
    while n:
        print('n =', n)
        # 3의 배수라서 자리수가 넘어가야될 때, 넘어가지 않도록 1을 빼주고, 0대신 4로 표시
        if n % 3 == 0:
            print(str(n) + '(3의 배수)을 3으로 나눈 나머지: 0->4, 몫:', n // 3, '- 1 =', n // 3 - 1)
            answer = str(4) + answer
            n = n // 3 - 1
        # n이 3의 배수가 아니라면
        # 3진법과 동일하게 3으로 나눈 나머지를 answer 문자열 앞에 저장, n에는 몫을 저장
        else:
            print(str(n) + '을 3으로 나눈 나머지:', str(n % 3) + ', 몫:', n // 3)
            answer = str(n % 3) + answer
            n = n // 3
    print()
    return answer

    # 남의 코드1 -> dataframe으로 출력
    # raw_data = { #'숫자': [],
    #             '3진법': [],
    #             '124나라': []}
    # # raw_data['숫자'] = list(range(21))
    # raw_data['3진법'] = list(convert(i, 3) for i in range(1, 21))
    # raw_data['124나라'] = list(solution_ref2(i) for i in range(1, 21))
    #
    # data = pd.DataFrame(raw_data, index= list(range(1, 21)))
    # # set_option('display.width', 100)
    # data.index.name = '숫자'
    # print(data)
    # # saving the excelsheet
    # file_name = '124_sheet.xlsx'
    # data.to_excel(file_name)


    # 남의 코드2
    # lst = ['1', '2', '4']
    # answer = ''
    # while n > 0:
    #     n -= 1
    #     answer = lst[n % 3] + answer
    #     n //= 3
    # return answer



# print('입력값:5, 결과:', solution(5), '-> 정답은 12', end='\n\n')
# print('입력값:6, 결과:', solution(6), '-> 정답은 14', end='\n\n')
print('입력값:9, 결과:', solution(9), '-> 정답은 24', end='\n\n')
print('입력값:10, 결과:', solution(10), '-> 정답은 41', end='\n\n')
# print('입력값:13, 결과:', solution(13), '-> 정답은 111', end='\n\n')

# solution(10)  # for dataframe 출력

# a = [i for i in range(10)]
# b = [convert(i, 3) for i in range(1, 21)]
# print(a)
# print(b)


# assert
# 조건식이 False인 경우, AssertionError예외가 발생한다.
# 조건식이 True인 경우 어떠한 메시지도 표시되지 않는다.
# https://engineer-mole.tistory.com/217
# assert solution(3) == '4', '정답은[{}], 결과값은[{}]'.format('4', solution(3))
# assert solution(4) == '11', '정답은[{}], 결과값은[{}]'.format('11', solution(4))
# assert solution(10) == '41', '정답은[{}], 결과값은[{}]'.format('41', solution(10))
# print('정답입니다.')

