from typing import List


class Solution(object):
    # mistaken attempt, only for orderly array
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            for right in range(len(nums) - 1, left, -1):
                if nums[left] + nums[right] > target:
                    continue
                elif nums[left] + nums[right] < target:
                    break
                else:
                    return [left, right]
