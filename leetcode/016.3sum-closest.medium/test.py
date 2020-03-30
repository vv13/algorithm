import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution
from typing import List


if __name__ == "__main__":
    inputs = [
        [[-1, 2, 1, -4], 1],
        [[0, 2, 1, -3], 1],
        [[1, 1, 1, 0], -100]
    ]
    testRunner(inputs, Solution)
