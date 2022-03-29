# https://www.acmicpc.net/problem/10799
from collections import deque

str = input()  # ()(((()())(())()))(())
strDot = str.replace('()','.')
# print(strDot)  # .(((..)(.).))(.)

lst = list(strDot)
deq = deque(lst)

# barDeq = deque()
bars = []    # 열리는 괄호들을 저장하는 리스트
barIdx = []  # 괄호시작 index를 저장하는 리스트
count = 0
for i in range(len(deq)):
    pop = deq.popleft()
    bars.append(pop)
    if pop == '(':
        # barIdx.append([i,None])  # 초기에는 쇠막대기 시작,종료idx를 배열로 넣으려했었음
        barIdx.append(i)
    if pop == ')':
        # print('괄호시작idx:',barIdx[-1],'괄호끝idx:',i)
        count += strDot[barIdx[-1]:i].count('.')+1  # 조각수 = 그 안에 있는 점갯수+1
        barIdx.pop()  # 조각수를 카운팅한 쇠막대기 idx는 삭제

    # print(barIdx)

print(count)