from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0

        for i in jewels:
            result += stones.count(i)

        return result

s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))

# 풀이4 문법
S = "aAAbbbb"
J = "abBCC"
print([s for s in S])
print(*(s for s in S))
print(list(S))
print([s in J for s in S])
