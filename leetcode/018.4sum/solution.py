'''
将 fourSum 转换为 threeSum 解决
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        if len(nums) < 4 or nums[-1] * 4 < target or nums[0] * 4 > target:
            return result
        for i in range(len(nums) - 3):
            first_num = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2, 1):
                second_num = nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                expect = target - first_num - second_num
                while left < right:
                    two_sum = nums[left] + nums[right]
                    if two_sum == expect:
                        result.append(
                            [first_num, second_num, nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif two_sum < expect:
                        left += 1
                    else:
                        right -= 1
        return result
