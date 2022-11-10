n, m = map(int, input().split())
lst = list(map(int, input().split()))

sum = 0
for i in range(len(lst) - 1):  # 공이 5개일때, 4번째 공에서 5번공 경우까지 계산하므로 -1 해줌
    print(f'\n{i+1}번공 골랐을 때 경우의 수:', len(lst[i+1:]) - lst[i+1:].count(lst[i]))
    print(f'나머지 공들', lst[i+1:], f'갯수에서 {i+1}번공 무게({lst[i]})와 같은 공 갯수 빼주기({len(lst[i+1:])}-{lst[i+1:].count(lst[i])})')
    sum += len(lst[i+1:]) - lst[i+1:].count(lst[i])

print(sum)