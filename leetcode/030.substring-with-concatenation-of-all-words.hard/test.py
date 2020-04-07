import sys
from os import path
sys.path.insert(0, path.abspath(path.join(__file__, '../../utility')))
from test_runner import testRunner

from solution import Solution


if __name__ == "__main__":
    inputs = [
        ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]],
        ["barfoothefoobarman", ["foo", "bar"]],
        ["wordgoodgoodgoodbestword", ["word", "good", "best", "good"]],
        ["ababaab", ["ab", "ba", "ba"]]
    ]
    testRunner(inputs, Solution)
