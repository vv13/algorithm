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
