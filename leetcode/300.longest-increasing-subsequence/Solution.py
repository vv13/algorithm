from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_num = 0
        store = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    store[i] = max(store[j] + 1, store[i])
            max_num = max(store[i], max_num)
        return max_num
