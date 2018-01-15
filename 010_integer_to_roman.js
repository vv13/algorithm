/**
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

 * @param {number} num
 * @return {string}
 */
var intToRoman = (num) => {
  const M = ['', 'M', 'MM', 'MMM'];
  const C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'];
  const X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'];
  const I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'];
  return M[parseInt(num / 1000)] + C[parseInt(num % 1000 / 100)] + X[parseInt(num % 100 / 10)] + I[parseInt(num % 10)]
};

// Runtime: 242 ms, beats 79.54%
