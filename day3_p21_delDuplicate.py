import collections

# https://daebaq27.tistory.com/39?category=921644
# https://velog.io/@minjung-s/remove-duplicate-letter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char) # set은 순서가 멋대로 들어감

        return ''.join(stack)

s = Solution()
print(s.removeDuplicateLetters('cbacdcbc'))
