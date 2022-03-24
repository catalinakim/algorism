# 프로그래머스 Level 2
def solution(dirs):
    count = 0
    path = []
    current = [0, 0]

    for i in dirs:
        new = current[:]
        if i == 'U':
            new[1] += 1
        elif i == 'D':
            new[1] -= 1
        elif i == 'L':
            new[0] -= 1
        elif i == 'R':
            new[0] += 1
        if abs(new[0]) > 5 or abs(new[1]) > 5:
            new = current[:] # 5넘어가면 제자리로 원복 -> 안해줘도 상관없네 ㅋㅋ어차피 new는 local
            # print('comeback')
            # pass
        else:
            if [current, new] in path or [new, current] in path:
                pass
            else:
                count += 1
                # print('처음가는길')
            # print(current, new)
            path.append([current, new])
            current = new

    return count

# 다른사람 풀이
# def solution(dirs):
#     s = set()
#     d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     x, y = 0, 0
#     for i in dirs:
#         nx, ny = x + d[i][0], y + d[i][1]
#         # print(nx, ny) # 5칸 넘어가는 좌표는 어차피 지역변수로만 있고 저장이 안됨, for새로돌때 사라짐
#         if -5 <= nx <= 5 and -5 <= ny <= 5:
#             s.add((x,y,nx,ny))  # set은 어차피 중복이면 안들어가니까
#             s.add((nx,ny,x,y))  # 왕복경로 저장
#             x, y = nx, ny
#     return len(s)//2
print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LRLRL"))  # 답은 1

''' 35점, 1/20~7/20 통과, 테스트 8/20~20/20 까지 통과가 안됨
이거 방향성이 없어야지 정답처리되네요. 
오른쪽에서 왼쪽으로 간거하고 왼쪽에서 오른쪽으로 간거하고 결국은 같은 길을 지난거니까 횟수에 넣어야함.
테스트 케이스 하나 남겨 놓습니다. "LRLRL" 1
'''