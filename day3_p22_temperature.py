from typing import List

# 혼자 풀기: fail -> 답이 틀리게 나옴
# 내가 풀려던 거랑 비슷한 풀이: https://weejw.tistory.com/520 but 시간초과 난다고 함
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = temperatures
        result = [0 for i in range(len(lst))]

        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] < lst[j]:
                    result[i] = j-i
                    continue
                else:
                    result[i] = 0
        return result

# 정답 : https://rollingsnowball.tistory.com/169
# 눈으로 보기 : https://www.youtube.com/watch?v=WGm4Kj3lhRI
class Solution2:
    def dailyTemperatures(self, tempList: List[int]) -> List[int]:

        # result = [0 for i in range(len(tempList))]  # for문 돌아서 시간 더 걸림
        result = [0] * len(tempList)
        stack = []  # pair: [온도, index번호]

        # enumerate : index, 원소로 이루어진 튜플 반환
        # list를 역순으로 : https://www.delftstack.com/ko/howto/python/python-iterate-list-backwards/
        for i, cur in list(enumerate(tempList))[::-1]:
            print(i, cur)
            # stack에 있는 미래온도가 현재온도보다 낮으면(미래온도가 더 추우면), stack에 있는 미래온도 버림
            while len(stack) and tempList[i] >= stack[-1][0]:
                stack.pop()
            # stack에 있는 미래온도가 더 따뜻하면, 날짜 차이 계산해서 결과에 넣기
            if len(stack) and tempList[i] < stack[-1][0]:
                distance = stack[-1][1] - i
                result[i] = distance
            stack.append([cur, i])

        return result

if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]

    sol = Solution()
    res = sol.dailyTemperatures(temperatures)
    # print(res)

    sol2 = Solution2()
    res = sol2.dailyTemperatures(temperatures)
    print(res)