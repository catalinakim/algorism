# https://programmers.co.kr/learn/courses/30/lessons/42747

# citations = [3, 0, 6, 1, 5]
citations = [31, 66]  # 2
# citations = [12, 11, 10, 9, 8, 1]  # 5
# citations = [6,6,6,6,6,1]   # 5
citations = [20,21,22,23] # 4


def solution(citations):
    answer = 0
    result = []

    # 내림차순으로 정렬
    citations.sort(reverse=True)
    print(citations)

    # 방법1, 테스트케이스만 통과, 제출시 런타임에러(ValueError: max() arg is an empty sequence)
    # for i in citations:
    #     if i == 0:
    #         continue
    #     newLst = [x for x in citations if x>=i]  # https://coding-groot.tistory.com/21
    #     if i == len(newLst):
    #         result.append(i)
    # answer = max(result)

    # 시도2 - 테스트 8,12만 통과
    # 모든 논문의 인용 횟수가 논문의 갯수보다 많을 때는 논문의 갯수를 return 해야 해요!
    # [20,21,22,23] => 4
    # [4,4,4] => 3
    for i in range(len(citations)):
        if i+1 > citations[i]:
            answer = i
            return answer
    # return answer
    return len(citations)

print(solution(citations))

# filter https://loklee9.tistory.com/127

# 실패 런타임 에러
# H 지수 : https://www.ibric.org/myboard/read.php?Board=news&id=270333

