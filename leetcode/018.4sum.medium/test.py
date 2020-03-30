import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution
from typing import List


if __name__ == "__main__":
    inputs = [
        [[-3,-2,-1,0,0,1,2,3], 0],
        [[-1,0,1,2,-1,-4], -1],
        [[0,4,-5,2,-2,4,2,-1,4], 12]
    ]
    testRunner(inputs, Solution)
