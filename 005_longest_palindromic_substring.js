/**
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

 * @param {string} s
 * @return {string}
 */
var longestPalindrome = (s) => {
  const sLen = s.length;
  const dp = [];
  for (let i = 0; i < sLen; i += 1) {
    dp[i] = new Array(sLen);
    dp[i][i] = true;
    if (s[i] === s[i + 1]) {
        dp[i][i + 1] = true;
    }
  }
  dp[sLen] = []
  let start = 0; 
  let end = 0;
  let max = 0;
  for (let i = sLen - 1; i >= 0; i -= 1) {
      for (let j = i; j < sLen; j++) {
          if (s[i] === s[j] && (j - i === 1 || dp[i + 1][j - 1])) {
              dp[i][j] = true;
              if (j - i > max) {
                  max = j - i;
                  start = i;
                  end = j;
              }
          }
      }
  }
  return s.slice(start, end + 1);
};

// Runtime: 647 ms, beats 3.98%
