from collections import deque

def sequence(docs, which, prio):
    # docs, which = map(int, input().split())
    # docs, which = 6, 0
    docs, which = docs, which
    # prio = list(map(int, input().split()))
    prio = prio

    order = 0
    idxList = [i for i in range(len(prio))]

    deq = deque(prio)
    idx = deque(idxList)

    while True:
        if deq[0] < max(deq):
            deq.append(deq.popleft())
            idx.append(idx.popleft())
        else:
            order += 1
            if idx[0]==which:
                break
            else:
                deq.popleft()
                idx.popleft()

    return order

n = int(input())
for i in range(n):
    docs, which = map(int, input().split())
    prio = list(map(int, input().split()))
    print(sequence(docs, which, prio))



