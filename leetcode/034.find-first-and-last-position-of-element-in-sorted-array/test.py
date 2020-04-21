import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution


if __name__ == "__main__":
    inputs = [
        [[5,7,7,8,8,10], 8],
        [[5,7,7,8,8,10], 6],
        [[4], 4],
        [[4, 4], 4],
        [[3, 4, 4], 4],
        [[4, 4, 5], 4],
    ]
    testRunner(inputs, Solution)
