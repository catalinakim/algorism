# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''

    if p == '':
        return ''

    def divUV(s):
        # u: 균형잡힌, 더이상 분리 불가
        # v: 빈 문자열 가능
        L, R = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                L += 1
            else:
                R += 1
            if L == R: # 균형맞음
                break
        return s[:L+R], s[L+R:]

    def isRight(u):
        L, R = 0, 0
        for i in u:
            if i == '(':
                L += 1
            else:
                R += 1
            if L < R:
                return False
        return True

    u, v = divUV(p)

    # 3번 조건
    if isRight(u):
        return u + solution(v)
    # 4번 조건
    else:
        answer += '('
        answer += solution(v) + ')'
        newU = u[1:-1]
        for i in newU:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer

# https://www.youtube.com/watch?v=P605nU1g7wM