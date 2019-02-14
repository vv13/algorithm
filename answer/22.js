/*
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
  const results = [];
  const start = "(";
  backTrace(results, start, n - 1, n);
  return results;
};

// 回溯法
function backTrace(results, current, left, right) {
  if (left > right) return;
  if (left === 0 && right === 0) {
    results.push(current);
    return;
  }
  if (left > 0) {
    backTrace(results, current + "(", left - 1, right);
  }
  if (right > 0) {
    backTrace(results, current + ")", left, right - 1);
  }
}
