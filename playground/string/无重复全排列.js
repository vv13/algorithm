/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
  const results = []
  const allPermutation = (nums, from, to, isRepeat) => {
      if (from === to) {
          results.push(nums.slice(0))
      } else if (from < to) {
          for (let i = from; i <= to; i++) {
              if (isWrap(nums, from, i)) {
                  [nums[i], nums[from]] = [nums[from], nums[i]];
                  allPermutation(nums, from + 1, to);
                  [nums[i], nums[from]] = [nums[from], nums[i]];
              }
          }
      }
  }       

  allPermutation(nums, 0, nums.length - 1);
  return results;
}

function isWrap(nums, start, end) {
 for (let i = start; i < end; i++ ) {
     if (nums[i] === nums[end]) return false
 }
 return true
}
