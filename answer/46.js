/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  const results = []
  const allPermutation = (nums, from, to) => {
      if (from === to) {
          results.push(nums.slice(0))
      } else if (from < to) {
          for (let i = from; i <= to; i++) {
              [nums[i], nums[from]] = [nums[from], nums[i]];
              allPermutation(nums, from + 1, to);
              [nums[i], nums[from]] = [nums[from], nums[i]];
          }
      }       
  }
  allPermutation(nums, 0, nums.length - 1)
  return results
};
