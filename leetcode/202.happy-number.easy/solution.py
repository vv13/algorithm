class Solution:
    def isHappy(self, n: int) -> bool:
        map = {}
        while n != 1 and n not in map:
            map[n] = 1
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
