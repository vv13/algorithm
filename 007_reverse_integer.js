/**
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 * @param {number} x
 * @return {number}
 */
const reverse = x => {
  const number = parseInt(
    (x > 0 ? '' : '-') +
      Math.abs(x)
        .toString()
        .split('')
        .reverse()
        .join('')
  );
  if (Math.abs(number) >= 2147483647) return 0;
  return number;
};

// Runtime: 146 ms, beats 39.65%
