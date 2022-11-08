# 스택 구현해보기
class Stack:
    def __init__(self):
        self.lst = []

    def push(self, data):
        self.lst.append(data)

    def pop(self):
        if self.isEmpty() == False:
            return self.lst.pop()
        return None

    def isEmpty(self):
        if len(self.lst) == 0:
            return True
        return False

# 노드로 구현해보기
class Node:
    def __init__(self, data):
        self.data = data

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

assert stack.pop() == 5
assert stack.pop() == 4
assert stack.pop() == 3
assert stack.pop() == 2
assert stack.pop() == 1
assert stack.pop() is None
assert stack.isEmpty()