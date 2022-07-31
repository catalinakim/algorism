from collections import deque
# deque : 양쪽에서 추가/삭제하는 리스트류 컨테이너
# https://docs.python.org/ko/3/library/collections.html#collections.deque

class MyStack():

    def __init__(self):
        self.deq = deque()

    def push(self, x: int) -> None:
        self.deq.append(x)

    def top(self) -> int:     # 스택은 마지막꺼가 top이므로
        data = self.deq.pop() # 오른쪽 꺼가 top, top을 임시 저장
        self.deq.append(data) # top을 조회만 할꺼니까 다시 추가
        return data           # top 리턴

    def pop(self) -> int:
        return self.deq.pop()
        # return self.deq[-1]  # 책

    def empty(self) -> bool:
        if len(self.deq)==0:
            return True
        else:
            return False

myStack = MyStack()
myStack.push(1)       #  앞 1
myStack.push(2)       #  앞 1 2
print(myStack.top())  # return 2
print(myStack.pop())  # return 2
print(myStack.empty())  # return False

