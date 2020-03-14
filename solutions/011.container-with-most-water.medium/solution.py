from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max = 0
        while l < r:
            ret = min(height[l], height[r]) * (r - l)
            if ret > max:
                max = ret
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max
