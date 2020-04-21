from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                exchange = len(nums) - 1
                while nums[i - 1] >= nums[exchange]:
                    exchange -= 1
                nums[i - 1], nums[exchange] = nums[exchange], nums[i - 1]
                index = i - 1
                break
        if index is None:
            nums.reverse()
            return nums
        for i in range(index + 1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


        