# 도토리 day1 - 링크드리스트 구현하기
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        if self.head is None: # == isEmpty()
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self): # 꼬리 삭제 및 꼬리값 반환
        data = self.tail.data # 비었을때 실행시 에러?
        # if self.head is None: # 아예 비어있으면
        if self.size == 0:
            print('아예 비어있음')
            return None
        # elif self.head.next is None: # 헤드만 있고 그 다음이 없으면
        elif self.size == 1: # 헤드만 있고 그 다음이 없으면
            print('헤드만 있음')
            data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return data
        else:
            print('요소가 2개 이상')
            node = self.head
            for i in range(self.size):
                if node.next == self.tail:
                    node.next = None
                    break
                node = node.next
            self.size -= 1
            return data
            '''
            # 2개일때 삭제가 안되는 코드 -> 갯수 4개인데, 3개를 삭제하는 코드...fail
            # while로 꼬리의 전까지 가서? 꼬리 앞의 next를 none으로, 꼬리로 지정해야
            node = self.head
            # while node.next.next: # 'NoneType' object has no attribute 'next'
            while node.next:
                # 갯수가 3개이고, 현재노드의 다음다음이 꼬리이면
                if node.next.next is not None and node.next.next == self.tail:
                    node.next.next = None
                    self.tail = node.next
                else: # 갯수가 2개이면 - 갯수가 4개인데 else를 타네... 
                    print('else')
                    node.next = None
                    break
                node = node.next
            self.size -= 1
            return data
            '''

    def getHead(self):
        return self.head.data

    def delHead(self): # 헤드 삭제만, 반환값 X(True, false?)
        # 한개만 있어도 정삭작동, 리스트가 비어있으면 예외처리
        if self.size > 0:
            # 헤드를 현재 헤드의 다음꺼로 지정, 기존헤드 삭제
            temp = self.head
            # print(id(self.head))
            # print(id(temp))
            self.head = self.head.next
            # print('_삭제할 헤드:',temp.data)
            self.size -= 1
            del temp  # 객체(변수)를 삭제
            return True
            # print(temp.data)
            # local variable 'temp' referenced before assignment 할당 전에 변수가 참조 될 때 발생
        return False


    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def __str__(self): # 링크드리스트 요소 헤드부터 출력
        lst = []
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next
        return str(lst)

# node = Node(2)
link = LinkedList()
link.add(4)
link.add(5)
link.add(6)
print(link)
print('size:',link.size)
print()
# print('헤드:', link.head.data)
# print('꼬리:', link.tail.data)
# print('헤드:', link.getHead())
print('delHead결과:',link.delHead())
print('delHead결과:',link.delHead())
# print('delHead결과:',link.delHead())
# print('delHead결과:',link.delHead())
print(link)
print('size:',link.size)
print()
# link.add(7)
# link.add(8)
print(link)
print('pop된 데이터:',link.pop())
print('pop후',link)
print('size:',link.size)

# + 인덱스로 얻기get nth node, 인덱스로 중간에 추가, 리버스(외우기), 합치기
# 기술면접, 깃헙 포크, 서버리스, 모르면 모른다


# 테스트
# n = Node(1, 'a')
# print(n.data)
# print(n.next)
