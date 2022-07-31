from typing import List
import string

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # result = []

        alphaList = string.ascii_lowercase
        alphaDict = {}

        for i in range(2, 10):
            if i == 7 or i == 9:
                alphaDict[i] = alphaList[(i-2)*3 : (i-2)*3+4]
            else:
                alphaDict[i] = alphaList[(i-2)*3 : (i-2)*3+3]
        print(alphaDict)

        '''
        # 이중 for 1번째 - fail
        # for i in range(len(target)):
        for i in range(1):
            for j in range(len(target[i])):
                # result.append([target[i][i]]*len(target[i]))
                result.extend(([target[i][j]] * len(target[i])))
        print(result)
        print(target[-1])
        # for i in range(len(target[-1])):
        #     for j in range(len(result)):
        # for j in range(len(result)):
        #     for i in range(len(target[-1])):
        #         print(j)
        #         result[j] = result[j]+target[-1][i]
        #         print(result[j]) 
        # 2중 for 2번째 - 케이스 1만 해당
        # for i in target[0]:
        #     for j in target[1]:
        #         result.append(i+j)
        #
        # return result '''

        target = []  # [['a', 'b', 'c'], ['d', 'e', 'f']]
        for i in digits:
            target.append(list(alphaDict[int(i)]))

        # 재귀 만들어보기-> RecursionError: maximum recursion depth exceeded in comparison
        def rec(num):
            # 1. 변수 선언
            result = []
            # 2. 탈출 조건
            if num > len(target):
                return
            # 3. 연산
            # 4. 재귀 호출
            for i in range(len(target)): # 0,1 - 0
                for j in range(len(target[i])): # 0
                    str = target[i] + rec(i+1)
                    print(str)
                    i += 1
                # result.append(str)
            # 5. 결과값 리턴
            return result
        # rec(0)

    # neetcode
    def letterCombinations2(digits: str) -> List[str]:
        res = []
        digitToChar = {"2": "abc", "3": "def", "4": "ghi", # 그냥 문제에서 복붙..
                       "5": "jkl", "6": "mno", "7": "qprs",
                       "8": "tuv", "9": "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:  # 'abc'
                print('i:', i, ',c:', c, '->back(', i + 1, ',', curStr + c, ')')
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

    digit = '23'
    print(letterCombinations2(digit))


s = Solution()
print(s.letterCombinations(digits = "23"))

# 테스트 -----------------
# print('_____')
str = 'test'
# print(len(str))

# for i in ['a','b','c']:
#     for j in ['d','e','f']:
#         print(i+j)