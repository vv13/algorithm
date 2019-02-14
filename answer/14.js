/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = (strs) => {
  if (!strs.length) return ''
  if (strs.length === 1) return strs[0]
  if (strs.includes('')) return ''
  strs.sort((a, b) => a.length - b.length)

  const str1 = strs[0]
  const combineStr = strs.join('')
  const maxLen = str1.length
  const strIndex = strs.map((e) => e.length)
  const strsNum = strIndex.length

  let i = 0
  for (; i < maxLen; i++) {
    let currentChar = str1.charAt(i)
    let currentIndex = i
    for (let j = 0; j < strsNum; j++) {
      currentIndex += strIndex[j]
      if (currentIndex >= combineStr.length) {
        currentIndex = i
        continue
      }
      if (combineStr.charAt(currentIndex) !== currentChar) {
        return str1.slice(0, i)
      }
    }
  }
  return str1.slice(0, i)
}
