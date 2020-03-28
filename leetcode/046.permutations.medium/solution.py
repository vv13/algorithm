from typing import List
from itertools import permutations


class Solution:
    # 使用自带工具函数进行生成
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
