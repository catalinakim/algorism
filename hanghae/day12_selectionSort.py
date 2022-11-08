# 선택정렬 구현해보기
def select(lst):
    for i in range(len(lst)-1):
        for j in range(1, len(lst)-i):
            if lst[i] > lst[i+j]:
                lst[i], lst[i+j] = lst[i+j], lst[i]
        print('_',lst)

    return lst
# 되긴 됬는데, 선택정렬이 아닌가?
# 최소값을 찾으면서, 중간에 찾은 lst[i]보다 작은애를 발견할때마다 swap을 해주는군

# 선택정렬 완성본
def select2(lst):
    for i in range(len(lst)-1):
        minTemp = i  # 최소값을 찾기 위해 한번 도는 중에 최소값 index 임시저장
        for j in range(1, len(lst)-i):
            # if lst[i] > lst[i+j]:
            #     if lst[minTemp] > lst[i+j]:
            #         print(f'i: {i}, i+j: {i+j}, temp: {minTemp}')
            #         minTemp = i+j
            if lst[i] > lst[i+j] and lst[minTemp] > lst[i+j]:  # 상동
                # print(f'i: {i}, i+j: {i+j}, temp: {minTemp}')
                minTemp = i+j
        # print('minIdx:',minTemp)
        lst[i], lst[minTemp] = lst[minTemp], lst[i]
        # print('_',lst)

    return lst

# print(select([4, 6, 2, 9, 1]))
print(select2([4, 6, 2, 9, 1]))