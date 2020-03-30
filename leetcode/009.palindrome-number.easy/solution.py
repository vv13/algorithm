import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False
        s = str(x)
        slen = len(s)
        for i in range(math.ceil(slen / 2)):
            if s[i] != s[slen - 1 - i]:
                return False
        return True
