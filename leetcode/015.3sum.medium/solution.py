'''
将 threeSum 转为 twoSum 问题
'''
from typing import List


class Solution:
    # Time Limit Exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for index, a in enumerate(nums):
            map = {}
            for offset in range(index + 1, len(nums), 1):
                b = nums[offset]
                c = -a - b
                if c in map:
                    three_sum = sorted([a, b, c])
                    if three_sum in result:
                        continue
                    result.append(three_sum)
                else:
                    map[b] = offset
        return result
