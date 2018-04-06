/**
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
  const len = nums.length
  const results = []
  nums.sort((a, b) => a - b)
  const max = nums[len - 1]
  if (!nums || len < 4 || (4 * nums[0] > target) || 4 * max < target) return results

  for (let i = 0; i < len; i++) {
    const num = nums[i]
    if (i > 0 && num === nums[i - 1]) continue // duplicate
    if (num + 3 * max < target) continue // too small
    if (4 * num > target) break // too large
    if (4 * num === target) { 
      if (i + 3 < len && nums[i + 3] === num) {
        results.push([num, num, num, num])
      }
      break
    }
    threeSum(nums, results, i + 1, target - num)
  }
  return results
}

var threeSum = (nums, results, start, target) => {
  const len  = nums.length - 1
  const max = nums[len]
  if (3 * nums[start] > target || 3 * nums[len] < target) return

  for (let i = start; i < len; i += 1) {
    if (i > start && nums[i] === nums[i - 1]) continue
    let low = i + 1
    let high = len
    const sum = target - nums[i]
    while(low < high) {
      if (nums[low] + nums[high] === sum) {
        results.push([nums[start - 1], nums[i], nums[low], nums[high]])
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
}
