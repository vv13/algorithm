class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        max_len = 0
        start = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and len(stack):
                stack.pop()
                if len(stack):
                    max_len = max(max_len, i - stack[-1])
                else:
                    max_len = max(max_len, i - start + 1)
            else:
                start = i + 1
        return max_len
