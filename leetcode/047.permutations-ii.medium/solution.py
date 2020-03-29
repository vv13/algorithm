from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def sort(nums, res: List[int], start):
            if start == len(nums):
                res.append(nums[:])  # 需深拷贝
                return
            changed = {}
            for i in range(start, len(nums)):
                if nums[i] in changed:
                    continue
                else:
                    changed[nums[i]] = True

                nums[start], nums[i] = nums[i], nums[start]
                sort(nums, res, start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        sort(nums, res, 0)
        return res


if __name__ == "__main__":
    result = Solution().permuteUnique([3, 2, 2])
    print(result)
