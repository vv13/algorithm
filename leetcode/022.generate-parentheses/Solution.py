# 回溯法
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backTrace(result, current, left, right):
            if left > right:
                return
            elif left == 0 and right == 0:
                result.append(current)
                return
            if left > 0:
                backTrace(result, current + '(', left - 1, right)
            if right > 0:
                backTrace(result, current + ')', left, right - 1)

        result = []
        start = '('
        backTrace(result, start, n - 1, n)
        return result
