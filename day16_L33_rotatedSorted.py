# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            return -1


nums = [4,5,6,7,0,1,2]
target = 0
s = Solution()
s.search(nums, target)

'''
리스트에서 해당 값이 존재하는지 여부를 찾아주는 
list.index() 메소드가 O(1)의 시간 복잡도를 가진다는 것을 알고 있었고 
그렇기 때문에 문제는 3-4줄이면 정답을 제출 할 수 있었다. 

파이썬에서는 위와 같이 피벗을 쉽게 구할 수도 있겠지만, 
이진 탐색을 학습하는 중에 있기 때문에 이진 탐색을 활용하여 피벗을 구한다.
https://bellog.tistory.com/150 '''
