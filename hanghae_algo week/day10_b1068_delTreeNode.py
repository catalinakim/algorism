# 아이디어 ------ 틀렸습니다 not solved
# 리스트에서 삭제할 번호 인덱스의 값을 None으로 만들기 위해
# 그 번호가 부모인 자식, 그 자식이 부모인 애들, 마지막 자식까지 찾고 올라오면서 부모정보를 None으로 만들기 - 첫 재귀 성공!
# 트리만들고, 리프 갯수 구하기
n = int(input())
lst = list(map(int, input().split()))
d = int(input())

# n = 9
      # 0  1  2  3  4  5  6  7  8
# lst = [-1, 0, 0, 2, 2, 4, 4, 6, 6] # 4가 부모인 애들, 5,6이 부모인 애들, 6이 부모인 애들
# d = 4  # 인덱스번호
# dvalue = lst[d]
# 값을 바꾸려면 인덱스 필요
# print(lst.index(d)) # 앞에꺼 index 하나만 반환, 없으면 에러

# 재귀 무한반복시 디버그용
# import sys
# sys.setrecursionlimit(10)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def make_tree_by(lst, idx):  # idx: 부모로 할 녀석 인덱스
#     parent = None
#     if idx < len(lst):    # 주어진 리스트보다 더 생성을 할 수 없는거니까
#         value = lst[idx]  # index에 있는 값을 꺼내서 -> 트리구조를 만들어(TreeNode)
#         if value is None: # == -> is 가 문법에 맞아
#             return
#         # idx 0을 기준으로 왼쪽 자식, 오른쪽 자식 만들기 / 재귀적으로
#         parent = TreeNode(value)
#         parent.left  = make_tree_by(lst, 2 * idx + 1)  # 2*idx == 2를 곱하면 왼쪽자식의 직전노드
#         parent.right = make_tree_by(lst, 2 * idx + 2)
#
#     return parent
# global count
count = 0
def treeByParent(lst, idx):  # idx: 부모로 할 녀석 인덱스
    global count
    # count = 0
    parent = TreeNode(idx)
    # print(f'->func idx:{idx}')
    # if True in lst: # None이 아닌 숫자가 있으면
    if idx not in lst: # 트리노드?-----------
        # nonlocal count
        if lst[idx] != None:
            count += 1
            # print(f'<-리프? return TreeNode({idx})')
            return parent
        else: # 부모가 None이니까 그냥 리턴
            # print('<-just return')
            return
    if idx < len(lst):    # 주어진 리스트보다 더 생성을 할 수 없는거니까
        if idx in lst:
            idxNo = lst.index(idx)
            # print(f'idxNo: {idxNo}')
            if idxNo is None: # == -> is 가 문법에 맞아
                return
            parent.left  = treeByParent(lst, idxNo)  # 2*idx == 2를 곱하면 왼쪽자식의 직전노드
            parent.right  = treeByParent(lst, idxNo+1)  # 2*idx == 2를 곱하면 왼쪽자식의 직전노드
            lst[idx] = None
            # print('_end')
    # print(f'return TreeNode({idx})')
    return parent


# 삭제할 노드를 부모로 하는 자식, 그 자식을 부모로 하는 자식을 재귀로 계속 찾아 내려가서, 그 자식을 부모로 하는 애가 없을 때(종료조건)까지
def findChild(n):
    # print(f'→rec func n:{n}')
    ## for 문의 끝에 도달 했을 때 해야할 부분 ##
    if n not in lst:
        # print('←return')
        return
    else:
        ## for 문 안에 원하는 동작 코드 ##
        for _ in range(lst.count(n)): # 부모정보리스트에 삭제할 노드(부모)가 존재하는 만큼 돌기
            if n in lst: # 삭제할 놈을 부모로 하는 애가 있으면
                # print(f'if {n} in lst')
                idx = lst.index(n) # 그 애 노드번호(idx)를 찾아서
                # print('idx:',idx)
                findChild(idx)  # 또 그애를 부모로 둔 자식이 있는지 찾기
                lst[idx] = None # (자식이 없는 애까지 돌고 나오면) 밑에 자식부터 부모정보를 None으로
                # print(f'←close & make {idx}th None',lst)
findChild(d)
lst[d] = None
# print(lst) # [-1, 0, 0, 2, None, None, None, None, None]

# 부모정보로 tree를 만들어야
# root = treeByParent(lst, 0)
root = treeByParent(lst, lst.index(-1))
print(count)
'''재귀 기본틀
# def basic(n, i=0):
#     if i == n:  #### for 문의 끝에 도달 했을 때 해야할 부분 ####
#         return
#     else:
#         #### for 문 안에 원하는 동작 코드 ####
#         print(i)
#         #####################################
#         #### 다음 for 문으로 진행하기 위한 코드 ###
#         basic(n, i + 1)
# for i in range(n):
#     print(i)'''

# 과제톡
# 딕셔너리에 연결정보를 넣어주기, 입력할때 간선 제외

# 틀렸습니다 https://settembre.tistory.com/370
# 루트 노드를 0으로 가정하고 계십니다.
# -1이 여러 번 호출되는 게 아니라 그 호출 순서가 반드시 첫 번째가 아닐수 있기 때문에 0번 노드를 루트 노드로 간주해선 안 되는 거였군요...