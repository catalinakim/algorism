# https://www.acmicpc.net/problem/2751

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()
print(*lst, sep='\n')

'''
Unpacking Operator * 를 사용하여 리스트를 구분자를 넣어 바로 출력하는 방법이다.
위와 같이 *를 사용해서 unpacking한 데이터로 전달해야 sep를 적용할 수 있다.

출처: https://earthteacher.tistory.com/111 [개발자를 위한 4차원 주머니]'''