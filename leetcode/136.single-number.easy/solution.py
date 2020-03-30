from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for num in nums:
            r ^= num
        return r


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 4, 2, 4, 3]
    ]
    for input in inputs:
        output = Solution().singleNumber(input)
        print(output)
