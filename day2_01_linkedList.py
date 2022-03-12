class ListNode:
    # def __init__(self, val, next):
    def __init__(self, val=0, next=None):  # 기본값을 지정
        self.val = val
        self.next = next  # next link (다음 인자를 가리킴)

        # 예시 )
        # L.head == a
        # a.next == b
        # b.next == c
        # c.next == none

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
        node.next = ListNode(val, None)  # 새로 하나 만들어서, 그 다음에 붙여준다

    # 삭제
    # 혼자 구현시, 'ListNode' object has no attribute 'head', while안에 2번 if가 위치하니 무한 루프 등 에러
    # 참고: https://velog.io/@jewon119/01.알고리즘-기초-Linked-List
    # 4가지의 경우의 수를 가짐
    # - node가 없는데 node 삭제를 요청 할 경우 : node가 없음을 출력함
    # - haed를 지우는 경우 : 임시값에 삭제할 Node인 head를 보관 ⇢ head의 다음 Node를 head로 교체 ⇢ 임시값에 저장된 원래 head를 삭제
    # - 중간 node를 지우는 경우 : 삭제할 node인 node.next를 찾기 ⇢ 삭제할 현재 노드(node.next)를 임시 값에 보관 ⇢ 현재 node(node.next)를 다음 노드로 교체 ⇢ 임시값 삭제
    # - 마지막 node를 지우는 경우 : 위와 동일
    def delete(self, data):
        node = self.head # local variable 'node' referenced before assignment
        # global node
        # node = self.head # name 'node' is not defined
        # 1. node가 없으면
        # if self.head is None:
        if not self.head:
            print('empty')
        # 2. head를 지우면
        if node.val == data:  # 1 = 1
            # 2-1
            # temp = node  # head주소값을 temp에 저장
            # self.head = node.next  # head의 다음 주소값을 head로 변경
            # del node  # 헤드 삭제
            # 2-2
            del self.head  # 헤드 삭제
            self.head = node.next # 헤드의 다음값을 헤드에 저장
        # 3. 중간꺼 삭제시
        while node.next:
            if node.next.val == data:  # 'ListNode' object has no attribute 'head'
                temp = node.next
                node.next = node.next.next
                del temp
            else:
                node = node.next

lst = [1,2,3]
# lst = [1]
l1 = LinkedList()
for e in lst:  # list에 있는 모든 요소들을 돌면서
    l1.append(e)
# print(l1)

l1.delete(2)
# print(l1)  # 디버그
