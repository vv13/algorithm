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
