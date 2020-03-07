/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
  let end = nums.length - 1;
  for (let i = 0; i <= end;) {
    if (nums[i] === val) {
        const r = nums[i];
        nums[i] = nums[end];
        nums[end] = r;
        end -= 1;
    } else {
      i += 1;
    }
  }
  return end + 1;
};
