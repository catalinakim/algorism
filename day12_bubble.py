# 버블소트 구현해보기(혼자+답안참고)
lst = [4, 6, 2, 9, 1]
def bubble(lst):
    for j in range(1, len(lst)): # 1,2,3,4
        # print('j:',j)
        # 점점 for문 범위를 줄이기 위해서 j만큼 빼줌
        for i in range(len(lst)-j): # 5-1, 5-2, 5-3, 5-4
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                # print(lst)
        # for문을 한바퀴 돌면 최대값이 맨 뒤에 있음
    return lst
# print(lst)  # 구현코드를 메소드로 안감싸면, 정렬된 리스트 출력됨
print(bubble(lst))
print(bubble([3, 2, 1, 5, 3, 2, 3]))

assert bubble([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]