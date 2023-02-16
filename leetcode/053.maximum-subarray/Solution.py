from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_value = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            max_value = max(max_value, cur)
        return max_value
