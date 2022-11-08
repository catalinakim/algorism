class MyCircularQueue:  # Wrong Answer 10번만에 accepted

    def __init__(self, k: int):
        self.max = k
        self.cir = [None]*k
        self.front = 0
        self.last = 0

    def enQueue(self, value: int) -> bool:
        try:
            if self.cir[self.last] is None:  # 원형큐가 비었을때
                self.cir[self.last] = value
                # print(value, ' input, last:', self.last)
                return True
            elif self.cir[(self.last + 1) % self.max] is None:
                self.cir[(self.last + 1) % self.max] = value
                self.last = (self.last + 1) % self.max
                # print(value, ' input, last:', self.last)
                return True
            else:
                return False
        except:
            return False

    def deQueue(self) -> bool:
        if self.cir[self.front] is None:
            return False
        else:
            # self.cir[self.front] = None
            # if self.front != 0:
            #     self.front = (self.front + 1) % self.max
            # print('de, front:', self.front)
            # return True
            if self.cir[(self.front + 1) % self.max] is None:
                self.cir[self.front] = None
            else:
                self.cir[self.front] = None
                self.front = (self.front + 1) % self.max
            return True

    def Front(self) -> int:  # empty면 -1 리턴
        if self.cir[self.front] is not None:
            return self.cir[self.front]
        else:
            return -1

    def Rear(self) -> int:
        # print('rear self.last:', self.last)
        if self.cir[self.last] is not None:
            return self.cir[self.last]
        else:
            return -1

    def isEmpty(self) -> bool:
        # return self.cir[self.front] is None
        return self.cir.count(None) == self.max

    def isFull(self) -> bool:
        # return self.last - self.front == (self.max - 1) # wrong
        return self.cir.count(None) == 0

circle = MyCircularQueue(3)
# print(circle.enQueue(1))  # return True
# print(circle.enQueue(2))  # return True
# print(circle.enQueue(3))  # return True
# print(circle.enQueue(4))  # return False
# print(circle.Rear())      # return 3
# print(circle.isFull())    # return True
# print(circle.deQueue())   # return True
# print(circle.enQueue(4))  # return True
# print(circle.Rear())      # return 4
# Case2
# print(circle.enQueue(6))
# print(circle.deQueue())
# print(circle.enQueue(6))
# print(circle.deQueue())  # True
# Case3
# print(circle.enQueue(3))
# print(circle.enQueue(9))
# print(circle.enQueue(5))
# print(circle.enQueue(0))
# print(circle.deQueue())
# print(circle.deQueue())  # True
# Case3 - isfull Wrong Answer
print(circle.enQueue(1))
print(circle.enQueue(2))
print(circle.enQueue(3))
print(circle.deQueue())
print(circle.deQueue())
print(circle.enQueue(4))
print(circle.enQueue(5))
print(circle.isFull())