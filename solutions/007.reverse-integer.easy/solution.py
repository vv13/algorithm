class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])
        return result if abs(result) < pow(2, 31) else 0

print(Solution().reverse(1239900))
print(Solution().reverse(-1239900))
