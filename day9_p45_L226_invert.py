# 답안 코드
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree_by(lst, idx):  # idx: 부모로 할 녀석 인덱스
    parent = None
    if idx < len(lst):    # 주어진 리스트보다 더 생성을 할 수 없는거니까
        value = lst[idx]  # index에 있는 값을 꺼내서 -> 트리구조를 만들어(TreeNode)
        if value is None: # == -> is 가 문법에 맞아
            return
				# idx 0을 기준으로 왼쪽 자식, 오른쪽 자식 만들기 / 재귀적으로
        parent = TreeNode(value)
        parent.left  = make_tree_by(lst, 2 * idx + 1)  # 2*idx == 2를 곱하면 왼쪽자식의 직전노드
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

# 리트코드 Input tip
# a = TreeNode(4, TreeNode(2,TreeNode(1),TreeNode(3)), TreeNode(7,TreeNode(6),TreeNode(9)))

o = Solution()
root = [4,2,7,1,3,6,9]
print(o.invertTree(make_tree_by(root, 0)))

# 재귀 LIFO

# if 노드 == 리프노드 : queue 추가 안함 => 속도 비슷