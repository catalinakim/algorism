from collections import deque

def solution(length, weight, truck_weights):
    answer = 0  # 초
    trucks = deque(truck_weights,len(truck_weights))
    bridge = deque([0]*length, length)

    total = 0  # 다리위 무게 계산
    # while len(trucks) > 0 or total != 0:
    while trucks or total != 0:
        total -= bridge[0]
        bridge.popleft()

        if len(trucks) > 0:
            # if sum(bridge) +trucks[0] <= weight:  # sum이 시간초과
            print('트럭에 올릴 수 있는지:', total, trucks[0])
            if total + trucks[0] <= weight:
                total += trucks[0]
                bridge.append(trucks.popleft())
            else:
                bridge.append(0)
        else:
            bridge.append(0)
        # print('__다리 위:', bridge)
        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

# 케이스1만 통과
def solution2(length, weight, truck_weights):
    answer = 0  # 초
    trucks = deque(truck_weights,len(truck_weights))
    bridge = deque([0]*length, length)
    print(trucks)
    print(bridge)

    while len(trucks) > 0:

        bridge.popleft()
        if sum(bridge)+trucks[0] < weight:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
        print('다리 위:', bridge)
        answer += 1

    return answer
# print(solution2(2, 10, [7,4,5,6]))
# print(solution2(100, 100, [10]))

# list, reverse()로도 풀 수 있음