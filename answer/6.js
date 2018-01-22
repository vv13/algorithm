/**
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = (s, numRows) => {
  let str = ''
  if (numRows <= 1) {
    return s
  }
  var arrs = []
  for (let i = 0; i < numRows; i++) {
    arrs.push([])
  }
  let incre = 1
  let index = 0

  for (let i = 0; i < s.length; i++) {
    arrs[index].push(s.charAt(i))
    if (index === 0) {
      incre = 1
    }
    if (index === numRows - 1) {
      incre = -1
    }
    index += incre
  }
  for (var i = 0; i < numRows; i++) {
    str += arrs[i].join('')
  }

  return str
}
