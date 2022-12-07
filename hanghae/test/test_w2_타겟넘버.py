import sys
sys.setrecursionlimit(20)

def solution(numbers, target): # 다른사람풀이보고 튜터디버그 후 이해 - not solved
    answer = 0

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
    def dfs(idx, sum):
        nonlocal answer
        print(f'idx: {idx}')
        if idx == len(numbers) and sum == target: # 5,5갔을때 idx는 원소갯수랑 똑같으니까
            answer += 1
            print('일치')
            return
        elif idx == len(numbers):
            print('합 일치X')
            return
        # 풀다만 my코드
        # for i in range(idx, len(numbers)):
        # if sum + numbers[idx] == target:
        #     print('if1')
        #     sum += dfs_bfs(idx+1)
        #     answer += 1
        # if sum - dfs_bfs(idx) == target:
        #     print('if2')
        #     sum -= dfs_bfs(idx)
        #     answer += 1
        # return sum
        # 다음 인덱스와 (앞에서부터) 지금까지의 합  ↗ ↙ ↖ ↘ → ← ∨ ∧  +1-1+1-1+1 이런식 출력가능?
        # 리스트(len=5)에서는 0~4까지의 합
        dfs(idx + 1, sum + numbers[idx]) # 0,0  1,1  2,2  3,3  4,4 ← 5,5 ←일치x  트리그림 왼쪽부터 보면 이해가 쉬움!
        dfs(idx + 1, sum - numbers[idx]) #                   <-  ← ↘ 5,3 ←일치
    dfs(0, 0)                            #                   > 4,2 → 5,3 ←일치
    return answer                        #                 ←    ←  ↘ 5,1 ←일치x
                                         #                3,1
print(solution([1, 1, 1, 1, 1], 3)) # 5
# print(solution([4, 1, 2, 1], 4))    # 2

# 다른사람 풀이
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# https://velog.io/@timointhebush/프로그래머스-타겟-넘버-DFS-BFS-Python
# https://velog.io/@ju_h2/Python-프로그래머스-level2-타겟넘버-BFSDFS  다양한풀이!!!
# https://jellysong.tistory.com/68   2nd풀이!!
# https://codermun-log.tistory.com/298   비슷!
# https://heytech.tistory.com/141  그림