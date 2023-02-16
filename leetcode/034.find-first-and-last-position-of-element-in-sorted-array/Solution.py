from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        index = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if index == -1:
            return [-1, -1]
        i = j = index
        while i > 0:
            if nums[i] != nums[i - 1]:
                break
            else:
                i -= 1
        while j < len(nums) - 1:
            if nums[j] != nums[j + 1]:
                break
            else:
                j += 1
        return [i, j]
