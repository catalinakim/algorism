
# 리스트 복사 테스트
a = ['a','b','c','d']
b = ['i','j']
c = ['x','y']

# a.append(b)   # ['a', 'b', 'c', 'd', ['ddd', 'j']]
a.append(b[:])  # ['a', 'b', 'c', 'd', ['i', 'j']]  슬라이싱 결과를 붙인거라, 이후 b변경사항 적용안됨

b[0] = 'ddd'
print(a)


