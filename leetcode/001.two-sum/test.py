import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution
from typing import List


if __name__ == "__main__":
    inputs = [[[2, 7, 11, 15], 9]]
    testRunner(inputs, Solution)
