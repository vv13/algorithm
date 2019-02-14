/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = (x) => {
  if (x < 0) {
    return false
  } else if (x < 10) {
    return true
  } else if (x % 10 === 0) {
    return false
  }
  let num = 0
  while (x > num) {
    num = num * 10 + x % 10
    x = parseInt(x / 10)
  }
  return x === num || x == parseInt(num / 10)
}
