# https://ihp001.tistory.com/143

# fixme
#  https://leetcode.com/problems/reverse-linked-list/
#  Q15. 역순 연결 리스트
#  연결 리스트를 뒤집어라.
#  입력 : 1 → 2 → 3 → 4 → 5 → NULL
#  출력 : 5 → 4 → 3 → 2 → 1 → NULL

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    # 삽입
    def __init__(self):  # 없으면 안써도 됨 or pass
        # self.head = ListNode(None, None)
        self.head = None
        # pass

    def append(self, val):
        if not self.head:  # head가 None이면(입력받은게 없으면)
            self.head = ListNode(val, None)  # 다음 화살표는 없고, 데이터만 넣기
            return
        # head가 있으면, 끝까지 가서 붙이기
        node = self.head  # 내가 지금 가리키고 있는 애가 head
        while node.next:  # 화살표가 있는 한
            node = node.next  # 계속 다음->다음->제일끝
        # 꼬리에서
        node.next = ListNode(val, None)

class Solution:
    def reverseListRecur(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            # print(prev.val)  # val이 null
            return reverse(next, node)

        return reverse(head)

    def reverseListList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def print_list(self,list):
        while list:
            if list.next:
                print(list.val, ' -> ', end='')
            else:
                print(list.val)
            list = list.next

# 클래스명칭().print_list(보고싶은연결리스트)
# ex) solution().print_list(Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
Solution().print_list(Solution().reverseListRecur(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

lst = [1,2,3,4,5]
l1 = LinkedList()
for e in lst:  # list에 있는 모든 요소들을 돌면서
    l1.append(e)
# Solution().reverseListRecur(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
# result = Solution().reverseListRecur(l1.head)
# print(result)  # 디버그 - 5,4,3,2,1 출력 확인
