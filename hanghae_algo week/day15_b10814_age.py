# https://www.acmicpc.net/problem/10814

n = int(input())
lst = []

for i in range(n):
    lst.append(list(input().split())) # 회원 나이, 이름 저장
# print(lst)

lst.sort(key = lambda x:(int(x[0]))) # 나이순으로 정렬(index 0)

for i in lst:
    # print(*i)       # 언팩킹★
    print(i[0],i[1])  # 상동★
    # print(str(i)) # ['21', 'Junkyu']

print('------0')
print(*lst, sep='\n')               # ['20', 'Sunyoung']

# https://dojang.io/mod/page/view.php?id=2292
for x, y in lst:                    # 20 Sunyoung  -- 정답★
    print(x, y)

# for문 한줄로 테스트
print('------1')
# print( i for i in lst)                 # <generator object <genexpr> at 0x
print( list(i for i in lst))             # [['20', 'Sunyoung'], ['21', 'Junkyu'],
print( *list(i for i in lst))            # ['20', 'Sunyoung']
print( j for j in list(i for i in lst))  # <generator object <genexpr> at 0x

print('------2')
print( *(i for i in lst) )                     # ['20', 'Sunyoung'] ['21', 'Junkyu']
print( *(i for i in lst), sep='\n')            # ['20', 'Sunyoung']
print( *(j for i in lst for j in i), sep='\n') # 20
print( str(j) for i in lst for j in i)         # <generator object <genexpr> at 0x
print( list(str(j) for i in lst for j in i))   # ['20', 'Sunyoung', '21', 'Junkyu',

print('------3')
print( "".join( str(i) for i in lst))              # ['20', 'Sunyoung']['21',
print( "".join( str(j) for i in lst for j in i ))  # 20Sunyoung21Junkyu
