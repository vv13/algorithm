class Solution:
    # Sliding Window
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = l = r = 0
        smap = {}
        slen = len(s)
        while l < slen and r < slen:
            if smap.get(s[r]):
                smap[s[l]] = False
                l += 1
            else:
                smap[s[r]] = True
                r += 1
                if r - l > ans:
                    ans = r - l

        return ans
