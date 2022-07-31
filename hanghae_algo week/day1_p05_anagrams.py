import collections
from typing import List

class Solution:
    def anagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

if __name__ == '__main__':
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    # print(s.anagrams(strs))

# 풀이 이해
a = 'catalina'
print(sorted(a)) # sorted는 list를 리턴
print(''.join(sorted(a)))

c = collections.defaultdict(list)
c['test'].append('hello')
c['test'].append('world')
c['abc'].append('america')
print(c)
print(c['test'])
print(list(c.values()))

