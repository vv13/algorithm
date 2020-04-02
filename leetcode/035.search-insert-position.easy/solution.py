from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        elif nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            if r - l == 1:
                if target <= nums[l]:
                    return l
                elif target <= nums[r]:
                    return r
                else:
                    return r + 1

            middle = (l + r) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle
            else:
                r = middle
        return 0
