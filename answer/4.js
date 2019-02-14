/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = (nums1, nums2) => {
  const nums = nums1.concat(nums2).sort((x, y) => (x >= y ? 1 : -1))
  const len = nums.length
  return len % 2 === 1 ? nums[Math.floor(len / 2)] : (nums[len / 2 - 1] + nums[len / 2]) / 2
}
