import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


if __name__ == "__main__":
    inputs = [
    ]
    expects = [2]
    testRunner(inputs, Solution().removeElement, expects)
