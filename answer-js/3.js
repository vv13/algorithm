/**
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
