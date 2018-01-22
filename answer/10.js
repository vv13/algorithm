/**
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
const isMatch = (s, p) => {
  if (!s || !p) {
    return false
  }
  const dp = new Array(s.length + 1)
  for (let i = 0; i <= dp.length; i += 1) {
    dp[i] = new Array(p.length + 1)
  }
  dp[0][0] = true
  for (let j = 1; j <= p.length; j += 1) {
    dp[0][j] = j > 1 && p[j - 1] === '*' && dp[0][j - 2]
  }

  for (let i = 1; i <= s.length; i += 1) {
    for (let j = 1; j < s.length; j += 1) {
      if (p[j - 1] !== '*') {
        dp[i][j] = dp[i - 1][j - 1] && (s[i - 1] === p[j - 1] || '.' === p[j - 1])
      } else {
        dp[i][j] = dp[i][j - 2] || ((s[i - 1] === p[j - 2] || '.' === p[j - 2]) && dp[i - 1][j])
      }
    }
  }
  return dp[s.length][p.length]
}
