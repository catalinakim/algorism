from typing import List
import operator

''' 문제: 빈도수 순위에서 2위 이상인 요소 추출 
Input: nums = [1,1,1, 2,2, 3,3,3,3, 100], k = 2  빈도수 -> {1: 3,  2: 2,  3: 4,  100: 1}
Output: [3, 1]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''문제가 k개 이상인거 추출인줄 알고 푼 코드
        # 중복제거를 위해 set형식으로 변환
        st = set(nums)
        result = []
        for s in st:
            if nums.count(s) >= k:
                result.append(s)
        return result'''
        st = set(nums)  # 중복제거를 위해 set형식으로 변환
        dct = {}
        for s in st:
            dct[s] = nums.count(s)  # 딕셔너리에 빈도수 저장
        # print(dct)  # {1: 3,  2: 2,  3: 4,  100: 1}

        # 파이썬 딕셔너리의 value로 정렬 : https://blockdmask.tistory.com/566
        # sorted가 list로 반환
        dctSorted = sorted(dct.items(), key=operator.itemgetter(1), reverse=True)  # reverse=True가 내림차순, key안쓰면 key기준 정렬
        # dctSorted = sorted(dct.items(), key=lambda x:x[1], reverse=True)
        # print(dctSorted)        # [(3, 4), (1, 3), (2, 2), (100, 1)]
        # print(dctSorted[0][0])  # 1

        result = []
        for i in range(k):  # 2위까지만 추출하면 되므로 k번
            result.append(dctSorted[i][0])
        return result

    def topKFrequentBook(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter  # 튜터닷컴
        import collections
        import heapq
        from typing import List
        freqs = collections.Counter(nums)  # 튜터닷컴은 출력문을 대입
        print(freqs)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

s = Solution()
nums = [1, 1, 1,  2, 2,  3, 3, 3, 3, 100]
k = 2
print(s.topKFrequent(nums, k))



# zip
# print(zip([1,2,3],['a','b','c','d']))
# print(list(zip([1,2,3],['a','b','c','d'])))
