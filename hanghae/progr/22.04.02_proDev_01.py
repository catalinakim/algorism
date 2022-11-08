# 행렬에 두 점 사이의 거리
# 행렬을 만족하는 경우의 수
import sys

sys.stdin = open("../input.txt", "r")

def solution(dist):
    answer = [[]]
    return answer

# lst = list(sys.stdin.readline())
lst = [[0,5,2,4,1],
       [5,0,3,9,6],
       [2,3,0,6,3],
       [4,9,6,0,3],
       [1,6,3,3,0]]
# lst = [[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]  # [[0,3,1,2],[2,1,3,0]]
solution(lst)
# [[1,2,0,4,3],[3,4,0,2,1]]

# 0부터 힙큐, 붙여나가서, 결과와 reverse한거

