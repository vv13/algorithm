from typing import List
from itertools import permutations


class Solution:
    # 使用自带工具函数permutations进行序列
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(list(nums))

    # 递归解法
    def permute1(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], res: List[int], path: List[int]):
            if not nums:
                res.append(path)
            else:
                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])
        res = []
        dfs(nums, res, [])
        return res

    # 交换数的位置
    def permute2(self, nums: List[int]) -> List[List[int]]:
        def sort(nums, res: List[int], start):
            if start == len(nums):
                res.append(nums[:]) # 需深拷贝
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                sort(nums, res, start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        res = []
        sort(nums, res, 0)
        return res

if __name__ == "__main__":
    result = Solution().permute2([3,2,4, 5, 7])
    print(result)

