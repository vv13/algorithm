/**

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

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
