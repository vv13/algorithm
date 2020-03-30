from typing import List
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = math.inf
        if len(nums) == 3:
            return sum(nums)
        for index, a in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                sum_three = sum([a, nums[left], nums[right]])
                if abs(target - sum_three) < abs(target - closest_sum):
                    closest_sum = sum_three
                    if sum_three == target:
                        return closest_sum
                if sum_three > target:
                    right -= 1
                else:
                    left += 1
        return closest_sum
