def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2): # i와 j가 끝에 다다르지 않는 동안
        if arr1[i] < arr2[j]:  # 작은걸 리스트에 추가
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # -> i나 j중에 하나가 끝에 닿아서 while이 끝나면
    # 남은 어레이를 마저 리스트에 넣기
    while i < len(arr1): # 만약에 i가 끝까지 안갔다면, 리스트에 추가
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

# 쪼개기 : 반복 -> 재귀
# 절반만
def mergesort(lst):
    if len(lst) <= 1: # 하나만 남았을때는 배열 그대로 반환
        return lst

    # 그게 아니면 아래 행동 반복
    mid = len(lst) // 2  # 몫을 기준으로 왼쪽, 오른쪽 나눠
    L = lst[:mid]
    R = lst[mid:]

    # 나눈걸 대상으로 mergesort를 하고,
    # 그 mergesort가 되었다는 대상으로 둘을 합쳐주면 됨
    # return merge(mergesort(L), mergesort(R))

    # 디버그를 걸기 위해 나눠서 쓰기
    L_sorted = mergesort(L)
    R_sorted = mergesort(R)
    return merge(L_sorted, R_sorted)

assert mergesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert mergesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]