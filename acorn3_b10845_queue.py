# https://www.acmicpc.net/problem/10845
# 0.5초
import sys

#입력을 파일로 설정: https://itcrowd2016.tistory.com/81
sys.stdin = open("input.txt","r")

class Node:
    def __init__(self, data):  # (self, data, next = None)  # next없을때 값
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self._front = None
        self._back = None
        self.count = 0

    def push(self, data):
        newNode = Node(data)
        if self.empty() == 1:  # if self.front is None
            self._front = newNode
            self._back = newNode
        else:
            self._back.next = newNode
            self._back = newNode
        self.count += 1
        ''' 
        node = self.front  # front > 1 > 2 > 3 -> x
        while node.next:
           node = node.next
           node.next = Node(data)'''
    def pop(self):
        # 'NoneType' object has no attribute 'data' -> 비었을때
        # print('self.front:',self.front)  # method

        if self._front is None:
            return -1
        data = self._front.data # 'NoneType' object----

        self._front = self._front.next
        self.count -= 1
        return data


        '''
        if self.front is None:
            return -1
        node = self.front
        self.front = self.front.next
        return node.data
        '''

    def size(self):
        return self.count
    def empty(self):
        if self.count == 0: # if self.front is None:
            return 1
        return 0
    def front(self): # front라는 변수명, 함수명이 둘다 존재하여 에러!!!
        # 'Node' object is not callable
        # 알고보니 dept라는 리스트와 dept라는 함수가 둘 다 존재하기 때문이었다.
        # 가급적이면 변수와 함수는 같은 이름을 사용하지 말자.
        # https://www.hides.kr/705 / https://codefather.tech/blog/python-object-is-not-callable/

        # if self.count > 0:
        #     return self._front.data
        # return -1
        if self._front is None:  # 상동
            return -1
        return self._front.data
    def back(self):
        if self.count > 0:
            return self._back.data
        return -1
        '''        
        node = self.front  # front > 1 > 2 > 3 -> x
        while node.next:
           node = node.next
           node.next = Node(data)
        return node.data
           '''

n = int(sys.stdin.readline())
# lst = []
q = Queue()
for _ in range(n):
    line = sys.stdin.readline().split()
    # lst.append(line)  # 생략가능
    order = line[0]
    if order == 'push':
        q.push(line[1])
    elif order == 'pop':  # -1이 나오네..
        print(q.pop())
    elif order == 'size':
        print(q.size())
    elif order == 'empty':
        print(q.empty())
    elif order == 'front':
        print(q.front())
        # print(q._front.data)  # 상동
    elif order == 'back':
        print(q.back())
        # print(q.queue[-1] if not q.empty() else -1)
    # 다른 풀이
    # order = input()
    # if 'push' in order:
    #     queue.append(int(order[5]))

# 제출시 런타임에러(NameError)
'''
왜 출력에 공백이 생기지?->개행문자 입력전이라(엔터전)
-> https://www.acmicpc.net/board/view/69012
0

3
'''

# queue모듈 에러: https://www.acmicpc.net/board/view/51521