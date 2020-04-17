import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution


if __name__ == "__main__":
    inputs = [
        [[4, 5, 6, 7, 1, 2, 3], 2],
        [[4, 5, 6, 7, 1, 2, 3], 4],
        [[4, 5, 6, 7, 1, 2, 3], 5],
        [[4, 5, 6, 7, 1, 2, 3], 6],
        [[4, 5, 6, 7, 0, 1, 2], 3],
        [[3, 1], 1]
    ]
    testRunner(inputs, Solution)
