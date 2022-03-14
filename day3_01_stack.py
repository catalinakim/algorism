class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    # push, pop, is empty
    def is_empty(self):
        return self.top is None

    def push(self, val):
        self.top = Node(val, self.top) # 기존의 Top을 next에 넣고, 이 노드를 새로운 Top로 지정

    def pop(self):
        if not self.top:  # top이 비어있으면 아무것도 반환하지 마
            return None

        node = self.top   # top을 꺼내서
        self.top = self.top.next  # top을 그 아래 있는 녀석으로 지정, 여기서 top이 None이면 None의 next는 에러남 -> 예외처리

        return node.item  # 그 값을 반환환

# My
class Node2:
    def __init__(self, data, next):
        self.data = data
        self.next = next
class Stack2:
    def __init__(self):
        self.top = None
    def add(self, data):
        self.top = Node2(data, self.top)
    def pop(self):
        if self.top is None:
            return None
        out = self.top
        self.top = out.next
        return out.data

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
result = stack.pop()
print(result)

stack2 = Stack2()
result = stack2.add(1)
result = stack2.add(2)
result = stack2.add(3)
result = stack2.pop()
print(result)

# 리스트로
lst = list()
lst.append(1)
lst.append(2)
lst.pop()
# print(lst)
