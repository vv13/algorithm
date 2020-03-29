class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        # 2d array
        dp = [[False] * sLen for i in range(sLen)]

        start = end = max = 0
        for j in range(sLen):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][i] = True
                elif i + 1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j] and j - i > max:
                    start = i
                    end = j
                    max = j - i
        return s[start:end + 1]

if __name__ == "__main__":
    testcase = 'asdfjsadjfkdslajasdfdsa'
    result = Solution().longestPalindrome(testcase)
    print(result)
