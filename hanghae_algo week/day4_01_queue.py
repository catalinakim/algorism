class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        if self.front is None:
            return None
        else:
            return False
        # T
        # return self.front is None

    def push(self, data):
        if self.front is None:
            self.front = Node(data, None)
        else:
            head = self.front
            while head.next:
                head = head.next
            head.next = Node(data, None)

    def pop(self):
        # T
        if not self.front:
            return None

        data = self.front.item

        self.front = self.front.next
        return data


queue = Queue()
# queue.push(1)
# queue.push(2)
# print(queue.pop())

# my 백준 2164 카드2 -> 시간초과
import sys
n = int(sys.stdin.readline().rstrip())  # 문자열의 오른쪽에서 공백or문자 제거
# n = int(input())

def myCard2(n):
    for i in range(n):
        queue.push(i+1)
    # for i in range(n-1):  # wrong
    #     if i%2 == 0: #인덱스 홀수번째
    #         print('pop:', i)
    #         queue.pop()
    #     else:
    #         print('push:', i)
    #         queue.push(queue.pop())
    while queue.front.next:
        queue.pop()
        queue.push(queue.pop())
# myCard2(n)
# print(queue.pop())

# T - 데크 : https://docs.python.org/ko/3/library/collections.html
from collections import deque

# deq = deque()
# for i in range(n):
#     deq.append(i+1)
# T
lst = [i+1 for i in range(n)]
lst = [i for i in range(1, n+1)]
print(lst)

deq = deque(i+1 for i in range(n))
deq = deque(i for i in range(1, n+1))

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())
print(deq.pop())
# T in method
# return deq.popleft()

test = list([0 for _ in range(6)])  # [0, 0, 0, 0, 0, 0]
print(test)
