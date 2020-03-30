import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution
from typing import List


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 8, 4, 7, 2, 9, 11, 12],
        [10, 9, 2, 5, 3, 7, 101, 18],
        [10, 9, 2, 5, 3, 4] 
    ]
    testRunner(inputs, Solution)
