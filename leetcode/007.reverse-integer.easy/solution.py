class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])
        return result if abs(result) < pow(2, 31) else 0


if __name__ == "__main__":

    testcase = [1239900, -1239900]
    for i in testcase:
    result = Solution().reverse(i)
    print(result)
