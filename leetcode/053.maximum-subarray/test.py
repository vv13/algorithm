import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution
from typing import List


if __name__ == "__main__":
    inputs = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ]
    testRunner(inputs, Solution)
