/**
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = (nums1, nums2) => {
  const nums = nums1.concat(nums2).sort((x, y) => (x >= y ? 1 : -1))
  const len = nums.length
  return len % 2 === 1 ? nums[Math.floor(len / 2)] : (nums[len / 2 - 1] + nums[len / 2]) / 2
}
