# 최대힙 구현 정답
class BinaryMaxHeap:
    def __init__(self):  # 클래스가 생성될때 실행되는 것 모음
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):  # 매직 메서드 : 예약되어 있다. 기본적으로 알고있는 함수를 덮어쓰기
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1  # -> 마지막에 넣은 요소의 인덱스를 알기 위해

    def _percolate_up(self):  # percolate:스며들다
        # 인덱스 제일 끝 값을 바라보게
        cur = len(self)    # 나의 길이를 구하라 했을때 __len__에서 1빼고 보내줌
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent는 항상 cur//2(몫)
        parent = cur // 2  # 부모의 위치(이거를 구하기 위해 인덱스를 1부터 시작함)

        while parent > 0:  # 부모의 index가 0이 되면 안되는거니까
            if self.items[cur] > self.items[parent]: # 내 값이 부모보다 크면, 위치 바꾸기
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            # parent가 0보다 클때까지 반복
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur): # 현재 (루트)위치에 있는 놈, 자식 둘 중에 가장 큰애를 위로 올려야
        # Index번호 의미
        biggest = cur  # 현재 (루트)위치에 있는 애를 가장 크다고 가정
        left = 2 * cur
        right = 2 * cur + 1
        # 부모(현재)와 왼쪽 자식과 비교, 왼쪽이 더 크면
        # left <= len(self) : left가 허용범위 내에 있고
        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left
        # 부모(현재)와 오른쪽 자식과 비교 --------- ??? <= 가 아니고 < 아닌가???? 7<=7
        if right <= len(self) and self.items[right] > self.items[biggest]: # 에러? 실행?
            print(f'len: {len(self)}, right: {right}')
            biggest = right
        # 위 두 연산이 끝나면, 자식중 큰 녀석이 biggest에 있을꺼야

        # cur과 biggest가 다르다는 것은, 위 두 연산중에 하나가 실행됬다는 뜻(= 부모보다 큰 자식이 있다는)
        if biggest != cur:
            # 가장 큰 녀석과 내 위치를 바꿔(오른쪽이든 왼쪽이든)
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest) # 가장 큰 녀석의 Index를 기준으로 다시 실행

    def insert(self, k):
        self.items.append(k) # 리스트에 집어넣기
        self._percolate_up() # 올린다

    def extract(self):
        if len(self) < 1: #추출할께없어
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]  # 루트와 젤 마지막에 있는 녀석 자리 바꿔주고
        self.items.pop()        # 루트를 빼주고
        self._percolate_down(1) # 루트자리에 간 녀석을 제자리에 갈 수 있게, 1 = 루트부터 살펴라

        return root

# 내가 풀어보기
class myMaxHeap:
    def __init__(self):
        self.lst = [None]
        self.len = len(self.lst) - 1  # __len__대신 이렇게 써도 되나?

    # def __len__(self):
        # 잘못쓴 코드(test)
        # self.len = len(self.lst) - 100  #여기서의 len은 기존 리스트의 len메서드인듯
        # return 50
        # 정답
        # return len(self.lst) - 1

    # def insert(self):
    #
    # def moveUp(self):
    #
    # def moveDown(self):
    #
    # def takeOut(self):

my = myMaxHeap()
print(my.len)

''' __len__에서 return 안할때 테스트
test = myMaxHeap()
# callable(object) : 전달받은 object 인자가 호출 가능한지 여부를 판단한다.
# print( test.len([1,2,3]) )  # 'int' object is not callable

print( test.len )  # 1-1 = 0
print( len(test) ) # 50
# len메서드에서 return을 안썼을때 에러: 'NoneType' object cannot be interpreted as an integer 논타입을 숫자로 해석할 수 없다!!
# --> 지금 len메서드에서 return을 안하니까, None을 반환해서 나오는 에러인듯!!
print( test.len )  # -99 오버라이드를 한 len에서 1-100 되어서 -99가 나오는 듯
print( len(test) ) # 50 메서드는 리턴값을 줌 ㅋㅋ '''

a = [1, 2, 3, 4]
a.reverse()
print(a)
b = [5, 6, 7, 8]
c = reversed(b)
print(b)
# print(list(c))
for i in c:    # 위에
    print(i)
print(reversed("abcde"))