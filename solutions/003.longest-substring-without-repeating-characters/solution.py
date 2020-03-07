class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        arr = []
        for i in s:
            if i in arr:
                if len(arr) > ans:
                    ans = len(arr)
                arr = arr[arr.index(i) + 1:]
            arr.append(i)
        return ans if len(arr) < ans else len(arr)

    # Sliding Window
    def lengthOfLongestSubstring1(self, s: str) -> int:
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
