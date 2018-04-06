/**
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = nums => {
  const results = []
  const len = nums.length
  if (len < 3) return results
  nums.sort((a, b) => a - b)
  for (let i = 0; i < len - 2; i += 1) {
    if (i > 0 && nums[i] === nums[i - 1]) continue
    let low = i + 1
    let high = len  - 1
    const sum = -nums[i]
    while(low < high) {
      if (nums[low] + nums[high] === sum) {
        results.push([nums[i], nums[low], nums[high]])
        while (low < high && nums[low] === nums[low + 1]) low += 1
        while (low < high && nums[high] === nums[high - 1]) high -= 1
        low += 1
        high -= 1
      } else if (nums[low] + nums[high] < sum) {
        low += 1
      } else {
        high -= 1
      }
    }
  }
  return results
}
