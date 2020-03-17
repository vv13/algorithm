from typing import List


class Solution(object):
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, cur in enumerate(nums):
            expect = target - cur
            if expect in map:
                return [index, map[expect]]
            map[cur] = index
