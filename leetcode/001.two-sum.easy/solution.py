from typing import List


class Solution(object):
    # brute force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

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

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, cur in enumerate(nums):
            expect = target - cur
            if expect in map:
                return [index, map[expect]]
            map[cur] = index
