# 문제. 입력받은 좌표값을 정렬
# 1. x좌표가 작은것 부터 출력한다.
# 2. x좌표가 같을 시 y좌표를 비교해 y좌표가 더 작은 것을 먼저 출력한다.

n = int(input()) # 좌표 갯수
lsts = []        # 좌표들을 저장할 리스트

# 입력된 x, y 좌표값을 리스트에 저장
for i in range(n):
    x, y = map(int, input().split())
    lsts.append([x,y])

print(lsts)

# 파이썬의 내장함수 sorted, 원본 값은 그대로이고 오름차순 정렬 값을 반환
# sortedList = sorted(lsts)

# key 매개변수 값은 정렬 목적으로 사용할 키를 반환하는 함수
# 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬
# 두 번째 인자를 기준으로 오름차순으로 정렬
# sortedList = sorted(lsts, key = lambda x : (x[0], x[1]))

# 좌표 정렬하기2
# 우선순위가 y값 기준으로 먼저 오름차순, x값 오름차순
sortedList = sorted(lsts, key = lambda x : (x[1], -x[0]))
# -는 내림차순
print(sortedList)

for i in range(n):
    print(*sortedList[i])  # asterisk(*) 리스트 괄호제거(Unpacking)
