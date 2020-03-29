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

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, first_num in enumerate(nums[:-2]):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            target = -first_num
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    result.append([first_num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
        return result

if __name__ == "__main__":
    testcase = [-1,0,1,2,-1,-4]
    result = Solution().threeSum(testcase)
    print(result)
