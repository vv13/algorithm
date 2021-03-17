import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))

from test_runner import testRunner
from solution import Solution
from typing import List


if __name__ == "__main__":
    # ret = Solution().combinationSum([2,3,6,7], 7)
    ret = Solution().combinationSum([2,3,5], 8)
    print(ret)
