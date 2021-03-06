class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            # expand(i, i+1)는 짝수 팰린드롬 판단, expand(i, i+2)는 홀수 팰린드롬 판단
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2), # 1, 3 -> while -> 0, 4 -> while -> return s[1:4] -> aba
                         key=len)
        return result

if __name__ == '__main__':
    s = Solution()
    str = "babad"
    print(s.longestPalindrome(str))

