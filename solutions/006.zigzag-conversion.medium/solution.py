class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        arrs = [[] for i in range(len(s))]
        incre = 1
        index = 0
        for i in range(len(s)):
            arrs[index].append(s[i])
            if index == 0:
                incre = 1
            elif index == numRows - 1:
                incre = -1
            index += incre
        return ''.join([i for item in arrs for i in item])


print(Solution().convert('PAYPALISHIRING', 6))
