from day2_01_linkedList import ListNode, LinkedList

class Solution():
    def __init__(self):
        pass

    def oddEvenList(self, head: ListNode)-> ListNode: # 1 2 3 4 5
        # head가 None이면
        if head is None:
            return None

        hol = head            # 1 -(while)- 3 -(while)- 5
        zzak = head.next      # 2 -(while)- 4 -(while)- None
        zzak_head = head.next # 2

        while zzak and zzak_head:
            hol.next = hol.next.next # 홀 next에 홀 다음다음꺼
            hol = hol.next           # 위에꺼를 hol에 대입

            zzak.next = zzak.next.next # 짝 next에 짝 다음다음꺼
            zzak = zzak.next           # 위에꺼를 zzak에 대입

        # 1,3,5 와 2,4 연결
        hol.next = zzak_head # 5의 next에 짝 주소값 저장

        return head

    def print_list(self, list: ListNode):
        while list:
            if list.next:
                print(list.val, ' -> ', end='')
            else:
                print(list.val)
            list = list.next

# 1,2,3,4,5를 linked list로 만들기 -> 1 3 5 2 4
lst = [1, 2, 3, 4, 5]
l1 = LinkedList()
for e in lst:
    l1.append(e)

result = Solution().oddEvenList(l1.head)
print(result)
Solution().print_list(result)

a, b = 1, 2
print(a, b)

