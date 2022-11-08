# ex. 아래 리스트를 적은 숫자 순으로 저장해서 리턴
# left = [0, 2]
# right = [1]
# ex. 아래 리스트를 적은 숫자 순으로 저장해서 리턴
left = [0, 2]
right = [1, 3]
lst = []
lp, rp = 0, 0
# while left or right:
while len(left) + len(right) != len(lst):
    print('lp', lp, 'rp', rp)
    # if len(left) == 0:
    if lp == len(left):
        lst += right[rp:]
        break
    if rp == len(right):
        lst += left[lp:]
        break
    if left[lp] < right[rp]:
        lst.append(left[lp])
        lp += 1
    else:
        lst.append(right[rp])
        rp += 1
    print(lst)
print(lst)