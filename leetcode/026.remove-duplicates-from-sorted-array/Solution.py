class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = 0
        for index in range(1, len(nums)):
            if nums[ret] != nums[index]:
                ret += 1
                nums[ret] = nums[index]
        return ret + 1
