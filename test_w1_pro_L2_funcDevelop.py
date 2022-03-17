from collections import deque

def solution(progresses, speeds):
    answer = []
    deq = deque()
    spd = deque()

    for i in progresses:
        deq.append(i)
    deq2 = deque(progresses)  # iterable바로 넣기!
    print(deq)
    print(deq2)
    for i in speeds:
        spd.append(i)

    days = 0
    # while len(deq) > 0:
    while deq:  # 상동
        today = 0
        nextOk = False
        for i in range(len(deq)):
            # 테스트케이스1만 통과
            # percent = deq.popleft()
            # speed = spd.popleft()
            # if i==0 and percent >= 100:
            #     print('if')
            #     today += 1
            # elif today>=1 and percent >= 100:
            #     today += 1
            #     print('elif', i)
            # else:
            #     print('else', i)
            #     deq.append(percent+speed)
            #     spd.append(speed)
            if (i==0 or nextOk is True) and deq[0] >= 100:
                deq.popleft()
                spd.popleft()
                today += 1
                if len(deq)>0 and deq[0] >= 100:
                    nextOk = True
                else:
                    nextOk = False
            # elif nextOk is True and deq[0] >= 100:
            #     deq.popleft()
            #     spd.popleft()
            #     today += 1
            else:
                # print(spd)
                deq.append(deq.popleft() + spd[0])
                spd.append(spd.popleft())
        days += 1
        # print('__day:', days, ', deq:', deq)
        if today >= 1:
            print('___배포', today)
            answer.append(today)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 이 문제는 deque보다 그냥 list 쓰시는게 더 빠릅니다
print('--다른사람 코드--')
print(-70//30)
print(70//30)
A = [[7, 1], [7, 2]]
print([a[1] for a in A])