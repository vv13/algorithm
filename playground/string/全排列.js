// 全排列

const executor = require('../executor');

const input = ['123'];

function main(str) {
  const charstr = str.split('')
  const result = []
  allPermutation(charstr, 0, charstr.length - 1, result);
  console.log(result)
}

function allPermutation(str, from, to, result) {
  if (from === to) {
    result.push(str.join(''))
  } else if (from < to) {
    for (let i = from; i <= to; i++) {
      [str[i], str[from]] = [str[from], str[i]]
      allPermutation(str, from + 1, to, result);
      // 还原操作
      [str[i], str[from]] = [str[from], str[i]]
    }
  }
}

executor(main, input);
