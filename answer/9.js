/**
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = (x) => {
  if (x < 0){
      return false;
  } else if (x < 10) {
      return true;
  } else if (x % 10 === 0) {
      return false;
  }
  let num = 0;
  while (x > num) {
      num = num * 10 + x % 10;
      x = parseInt(x / 10);
  }
  return x === num || x == parseInt(num / 10);
};
