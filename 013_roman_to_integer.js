/**
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

 * @param {string} s
 * @return {number}
 */
var romanToInt = s => {
  const numMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (numMap[s[i]] < numMap[s[i + 1]]) {
      sum -= numMap[s[i]];
    } else {
      sum += numMap[s[i]];
    }
  }
  return sum;
};

// Runtime: 275 ms, beats 46.92%
