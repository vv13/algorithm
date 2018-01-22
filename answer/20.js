/**
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

 * @param {string} s
 * @return {boolean}
 */
const isValid = (s) => {
  const stack = []
  const characters = ['(', '{', '[']
  const characterMap = {
    '}': '{',
    ']': '[',
    ')': '(',
  }
  for (let i = 0; i < s.length; i += 1) {
    let char = s.charAt(i)
    if (characters.indexOf(char) > -1) {
      stack.push(char)
    } else if (characterMap[char]) {
      if (stack.slice(-1)[0] === characterMap[char]) {
        stack.pop()
      } else {
        return false
      }
    } else {
      return false
    }
  }
  return !stack.length
}
