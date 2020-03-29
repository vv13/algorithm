from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_num = 0
        store = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    store[i] = max(store[j] + 1, store[i])
            max_num = max(store[i], max_num)
        return max_num


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 8, 4, 7, 2, 9, 11, 12],
        [10, 9, 2, 5, 3, 7, 101, 18],
        [10, 9, 2, 5, 3, 4] 
    ]
    for input in inputs:
        output = Solution().lengthOfLIS(input)
        print(output)
