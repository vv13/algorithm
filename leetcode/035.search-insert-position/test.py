import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution
from typing import List


if __name__ == "__main__":
    inputs = [
        [[1, 3, 5, 6], 2],
        [[1, 3], 3],
        [[1, 3, 5, 6], 5],
        [[1, 3, 4, 5, 6], 3]
    ]
    testRunner(inputs, Solution)
