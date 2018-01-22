/**
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = (s) => {
  let answer = 0
  let i = 0
  let j = 0
  const len = s.length
  const node = []
  while (i < len && j < len) {
    const char = s.charAt(j)
    if (!node.includes(char)) {
      node.push(char)
      j += 1
      answer = Math.max(answer, j - i)
    } else {
      node.shift()
      i += 1
    }
  }
  return answer
}
