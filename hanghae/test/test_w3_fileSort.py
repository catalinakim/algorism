# https://programmers.co.kr/learn/courses/30/lessons/17686

# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 정답:   ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# 내결과: ["IMG01.GIF","img12.png","img10.png","img02.png","img1.png","img2.JPG"]

# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# 정답: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

files = ['img100.p2ng', 'img202.png123']  # 1002 -> substring not found

# from curses.ascii import isalpha
# from unicodedata import numeric

import re
def solution(files):
    answer = []
    lst = []

    # for file in files:
    for idx, file in enumerate(files):
        # lst.append([idx, file.lower()])
        # lst.append([idx, re.sub(r'[^0-9]', '', file)])
        num = re.sub(r'[^0-9]', '', file)  # 파일명에서 숫자만 추출
        print(num)
        str = file[:file.index(num)]       # 숫자앞까지 문자열만 추출
        lst.append([idx, str.lower(), int(re.sub(r'[^0-9]', '', file).lstrip('0')), file])
        # 숫자추출 re: https://codechacha.com/ko/python-extract-integers-from-string/

    lst2 = sorted(lst, key = lambda x : (x[1], x[2]))
    # print(lst2)

    for i in range(len(lst2)):
        answer.append(lst2[i][3])

    return answer

print(solution(files))

# if not numeric: #숫자가 아니면
#     pass
# 자바에서는 각 파일명을 class Document로 각 객체로 만들어서, 각자 속성이 있음(파일명, head, tail 등등)

# 타인 코드
def solution(files):
    num_sort = sorted(files, key = lambda x : int(re.findall('\d+', x)[0]))
    str_sort = sorted(num_sort, key = lambda x : re.split('\d+',x.lower())[0])
    return str_sort

# 테스트 1 〉	통과 (0.11ms, 10.4MB)
# 테스트 2 〉	통과 (0.11ms, 10.3MB)
# 테스트 3 〉	실패 (런타임 에러)
# 테스트 4 〉	실패 (런타임 에러)
# 테스트 5 〉	실패 (런타임 에러)
# 테스트 6 〉	실패 (런타임 에러)
# [파이썬] 테스트케이스 많이틀리면 참고(스포주의) - https://programmers.co.kr/questions/12267
# [JAVA] 1,2번만 맞으시는분들 - https://programmers.co.kr/questions/13662
# 1~2 번 외에 다 틀려요.(불안정 정렬) - https://programmers.co.kr/questions/11988