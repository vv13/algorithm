class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        l_needle = len(needle)
        for i in range(0, len(haystack) - l_needle + 1):
            if haystack[i:i+l_needle] == needle:
                return i
        return -1

        