class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            '': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        prev = ''
        ret = 0
        for i in s[::-1]:
            ret += map[i] * (-1 if map[prev] > map[i] else 1)
            prev = i

        return ret
