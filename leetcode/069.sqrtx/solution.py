class Solution:

    def mySqrtV1(self, x: int) -> int:
        return int(x ** 0.5)

    # 使用二分法求解
    def mySqrtV2(self, x: int) -> int:
        if x <= 1:
            return x
        l = 0
        r = x
        while l < r:
            mid = (l + r) // 2
            if mid == l:
                return mid
            ret = mid ** 2
            if ret == x:
                return mid
            elif ret > x:
                r = mid
            elif ret < x:
                l = mid
        return l

    # The Babylonian square-root algorithm
    def mySqrtV3(self, x: int) -> int:
        if x <= 1:
            return x
        sqrt = int(x / 2)
        while sqrt * sqrt > x:
            sqrt = int((sqrt + x / sqrt) / 2)
        return sqrt
