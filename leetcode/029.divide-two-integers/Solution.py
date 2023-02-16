class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            sum = 1
            tmp = b
            while tmp + tmp < a:
                sum += sum
                tmp += tmp

            res += sum
            a -= tmp
        if not positive:
            res = -res
        return min(2147483647, max(-2147483648, res))
