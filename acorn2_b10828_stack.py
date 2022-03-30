# https://www.acmicpc.net/problem/10828

n = int(input())
lst = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # top했을때 'Node' object is not callable, 메소드명이랑 겹쳐서 그런듯
        ''' It's conventional in Python (see PEP-0008) prefix private fields (those that client code is not supposed to use)
            with an underscore, like so:
        def __init__(self):
            self._node = []
            self._prev = None
        It's also risky to name your class in lower case,
        since any variable named node will shadow it and make it inaccessible.
        https://stackoverflow.com/questions/32880318/typeerror-node-object-is-not-callable '''
        self._top = None
        self._count = 0
    # 메소드 만들어놓기
    def push(self, x):
        node = Node(x)
        if self.size() == 0:
            self._top = node
        else:
            node.next = self._top
            self._top = node
        self._count += 1

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            number = self._top.data
            self._top = self._top.next
            self._count -= 1

            return number

    def size(self):
        return self._count

    def empty(self):
        if self._count == 0:
            return 1
        else:
            return 0

    def top(self): # 예제2 'NoneType' object has no attribute 'data'
        if self.empty() == 1:
            return -1
        else:
            return self._top.data

stack = Stack()
for _ in range(n):
    # order = list(map(str, input().split()))
    order = list(input().split())  # 상동
    # print(order)  # ['push', '1']
    lst.append(order)
# print(lst)  # [['push', '1'], ['push', '2'], ['top'], ['size'], ['empty'], ['pop'], ['pop'], ['pop'], ['size'], ['empty'], ['pop'], ['push', '3'], ['empty'], ['top']]

# 리스트 받았다가 꺼내면서 하지 않고, input받자마자 바로 메소드 실행해도 됨
# but 일단은 리스트 받아서 하나씩 구현
for order in lst:
# for order in lst[:7]:
    if order[0] == 'push':
        stack.push(order[1])
    elif order[0] == 'pop':
        print(stack.pop())
    elif order[0] == 'size':
        print(stack.size())  # stack.order[0]
    elif order[0] == 'empty':
        print(stack.empty())
    elif order[0] == 'top':
        print(stack.top())