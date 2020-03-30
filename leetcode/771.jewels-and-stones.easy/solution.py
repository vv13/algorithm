class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count


if __name__ == "__main__":
    inputs = [
        ['aA', 'aAAbbbb']
    ]
    for input in inputs:
        output = Solution().numJewelsInStones(input[0], input[1])
        print(output)
