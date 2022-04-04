# https://www.acmicpc.net/problem/9375

import sys
sys.stdin = open("input.txt","r")

n = int(input())
for _ in range(n):
    dct = {}
    m = int(input())
    # if m == 0:
    #     print(0)
    for i in range(m):
        item, part = input().split()
        if part in dct.keys():
            dct[part].append(item)
        else:
            dct[part] = [item]
    mlt = 1  # multiple
    # if len(dct.keys()) > 1:
    #     for i in dct.keys():
    #         # print('_',len(dct[i]))
    #         mlt *= len(dct[i])
    #     print(m + mlt)
    # else:
    #     print(m)
    # 수정본
    for i in dct.keys():
        mlt *= (len(dct[i]) + 1)
    print(mlt-1)


# 0이 입력되었을때를 처리 -> 자동으로 0이 나왔었네 -> 수정본에서는 안써야 정답ㅋㅋ
# 옷 종류가 3개인 경우 오답이었음!
# 옷 종류가 3개가 있고 각 옷의 개수가 {2, 3, 4}벌 있다면 : https://www.acmicpc.net/board/view/20819
# !!각 아이템별로 경우의 수 계산(안입는 경우 포함)★ : https://st-lab.tistory.com/164