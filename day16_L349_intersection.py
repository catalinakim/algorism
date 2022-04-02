from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        inter = list(nums1 & nums2)

        return inter

# set.intersection()
# 다만 이 함수는 set타입에서 쓸 수 있어 list의 교집합을 구할 때는
# list를 set으로 변환해 set.intersection한 뒤, 그 결과를 다시 list로 변환해야 합니다.
# intersection = set1 & set2
# union = list(set(lst1) | set(lst2))
# union = list(set().union(lst1,lst2))



nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

s = Solution()
print(s.intersection(nums1, nums2))