def solution(lst, sec):
    result = 0

    quot = sec//len(lst)  #몫(quotient)
    rem = sec%len(lst)  #나머지(remainder)초
    left = len(lst)  #잔여음식 갯수

    if sum(lst) <= sec:
        result = -1
        return result

    while True:
        for i in range(len(lst)):
            if lst[i] > 0:
                if lst[i] > quot:
                    lst[i] -= quot
                elif lst[i] < quot:
                    rem += quot - lst[i]
                    lst[i] = 0
                    left -= 1
                else:  #섭취소요시간(초)와 몫과 같으면
                    lst[i] = 0
                    left -= 1
        # if left == 0:
        #     result = -1
        #     return result
        if rem < left:
            break
        elif rem >= left:
            quot = rem//left
            rem = rem%left

    for i in range(len(lst)):
        if rem == 0 and lst[i] > 0:
            result = i+1
            break
        elif lst[i] > 0:
            lst[i] -= 1
            rem -= 1

    return result


# 다른사람 코드(박)
def solution2(food_times, k):
    print('food_times', food_times)
    print('k',k, 'sum(food_times)', sum(food_times))
    if k>=sum(food_times):return -1
    times_sorted = sorted([(idx, val) for idx, val in enumerate(food_times)], key=lambda x: x[1])
    print(times_sorted)
    t = idx = 0
    n = len(food_times)
    cycle = times_sorted[0][1]
    while k-(n*cycle)>0:
        k -= n*cycle
        n -= 1
        idx += 1
        cycle = times_sorted[idx][1]-times_sorted[idx-1][1]
    return [i[0]+1 for i in sorted(times_sorted[idx:])][k%n]

food_times = [3, 1, 2]
k = 5
# food_times = [8,2,5]
# k = 10
print(solution(food_times, k))
print('food_times', food_times)
print(solution2(food_times, k))