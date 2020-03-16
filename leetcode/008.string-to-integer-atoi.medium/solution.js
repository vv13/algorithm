const myAtoi = (s) => {
  let index = 0
  let result = 0
  let signal = 1
  const MAX_NUMBER = 2147483647

  let str = s.trim()
  if (!str) return 0
  if (str[index] === '+') {
    signal = 1
    index++
  } else if (str[index] === '-') {
    signal = -1
    index++
  }
  while (index < str.length) {
    const number = str.charCodeAt(index) - '0'.charCodeAt()
    if (number > 9 || number < 0) break
    let tmpResult = result * 10 + number
    if (tmpResult > MAX_NUMBER) {
      return signal > 0 ? MAX_NUMBER : -MAX_NUMBER - 1
    }
    result = tmpResult
    index++
  }
  return result * signal
}
