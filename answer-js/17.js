/**
 * @param {string} digits
 * @return {string[]}
 */
const letterCombinations = (digits) => {
  if (digits.includes('0') || digits.includes('1') || !digits.length) return []
  const map = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
  const results = map[digits[0]].split('')

  for (let i = 1; i < digits.length; i++) {
    while (results[0].length === i) {
      const x = results.shift()
      for (const c of map[digits[i]].split('')) {
        results.push(`${x}${c}`)
      }
    }
  }

  return results
}
