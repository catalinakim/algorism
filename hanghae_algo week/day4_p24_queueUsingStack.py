# 그림: https://velog.io/@ny_/LeetCode-232.-Implement-Queue-using-Stacks

class MyQueue():

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> int:
        data = self.lst[0]
        del self.lst[0]
        return data

    def peek(self) -> int:  # peek: 큐의 시작부분
        return self.lst[0]

    def empty(self) -> bool:
        return len(self.lst) == 0

myQueue = MyQueue()
myQueue.push(1)   # queue is: [1]
myQueue.push(2)   # queue is: [1, 2](leftmost is front of the queue)
print(myQueue.peek())   # return 1
print(myQueue.pop())    # return 1, queue is [2]
print(myQueue.empty())  # return false