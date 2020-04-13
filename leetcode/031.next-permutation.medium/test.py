import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution


if __name__ == "__main__":
    inputs = [
        [5,4,7,5,3,2]
        # [1,5,1]
        # [1,3,2],
        # [2,3,1],
        # [],
        # [1, 2, 3],
        # [1,4,3,2],
        # [3,2,1],
        # [1,1,5],
        # [4,3,2,1]
    ]
    testRunner(inputs, Solution)
