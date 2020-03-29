from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        map_list = ['', '', 'abc', 'def', 'ghi',
                    'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = list(map_list[int(digits[0])])
        for i in range(1, len(digits), 1):
            while len(result[0]) == i:
                prefix = result.pop(0)
                for j in map_list[int(digits[i])]:
                    result.append(prefix + j)
        return result

if __name__ == "__main__":
    result = Solution().letterCombinations('234')
    print(result)
