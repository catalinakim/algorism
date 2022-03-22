# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    def maxDepth(self, lst):
        n = len(lst)
        return math.log2(n+1)-1

s = Solution()
print(s.maxDepth([3,9,20,None,None,15,7]))


# Leetcode에서는 입력이 TreeNode형태라 안되는 듯, not solved ----------

root = [4,2,7,1,3,6,9]


