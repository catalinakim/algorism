# https://leetcode.com/problems/binary-search/
import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        try:
            idx = nums.index(target)
        except:
            idx = -1
        return idx



nums = [-1,0,3,5,9,12]
target = 9

s = Solution()
rslt = s.search(nums, target)  # search() missing 1 required positional argument: 'target' -> 클래스 생성시 ()를 안써서
print(rslt)

# 리스트 메소드 시간복잡도 : https://mong9data.tistory.com/79
# Python 시간복잡도, 코드시간측정 : https://hbj0209.tistory.com/29
# python list index time complexity : https://stackoverflow.com/questions/5913671/complexity-of-list-indexx-in-python
#  - Its complexity is O(n)

idx = bisect.bisect_left(nums, 9)    # return value i is such that all e in a[:i] have e < x
idx2 = bisect.bisect_right(nums, 9)  # return value i is such that all e in a[:i] have e <= x
print(idx, idx2)

# Python builtin의 내부 코드를 보고 싶을 때
# : https://90byt.es/pycharmeseo-builtinyi-naebu-kodeureul-bogo-sipeul-ddae/
#   => https://github.com/python/cpython - 검색가능 in this repo
