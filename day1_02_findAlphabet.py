import string

word = input() # baekjoon

# 방법1. string모듈 활용
alphabetList = string.ascii_lowercase

# 방법2. 아스키코드 활용(a:97 ~ z:122)
# print(chr(97))  # 숫자를 아스키코드로 반환(character)
# print(ord('a')) # 문자를 아스키코드로 반환(ordinal)
alphabetList = list(map(chr, range(97, 122+1))) # ['a', 'b', 'c', 'd', 'e',

# abcdef~xyz에서 a부터 돌면서
for alphabet in alphabetList:
    # a가 word안에 있으면, 위치(index)를 출력, 아니면 -1 출력
    if alphabet in word:
        print(word.index(alphabet), end=' ')
    else:
        print(-1, end=' ')

# 선생님
# O(N^2)
def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase) # 알파벳 갯수길이 배열에 -1 집어넣기
    # print(result)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:  # 일치할 때 이미 안적었으면
                result[j] = i  # 'b'가 0번째(i)에 있으니까 0 집어넣기
    print(' '.join([str(num) for num in result]))  # 배열속 숫자를 문자로 바꾸고, 합치는데 사이를 공백으로

def get_idx(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        # ord: 문자(알파벳 대소문자)->숫자
        # 97 = ord('a')
        # idx = result에서 위치(몇번째)
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))


get_idx_naive('baekjoon')
# get_idx('baekjoon')
