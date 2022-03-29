# 삽입정렬 구현해보기
def insert(lst):
    for i in range(1, len(lst)): # 1,2,3,4 현재 들어온 신병 index
        for j in range(i-1, -1, -1): # 0 / 1,0 / 2,1,0
            # print(f'i:{i}, j:{j}')
            if lst[j] > lst[i]: # 내 왼쪽에 있는 요소가 더 크면, 자리 스왑
                lst[i], lst[j] = lst[j], lst[i]
            i -= 1  # 나의 index도 왼쪽으로 한칸 이동했으니 -1 해주기

    return lst

print(insert([4, 6, 2, 9, 1]))

for i in range(5,-1,-1):
    print(i)

assert insert([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insert([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]