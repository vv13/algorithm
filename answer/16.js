/**
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const threeSumClosest = (nums, target) => {
  nums.sort((a, b) => a - b)
  if (nums.length === 3) return nums.reduce((a, b) => a + b)

  let answer = nums[0] + nums[1] + nums[2]
  for (let i = 0; i < nums.length - 2; i++) {
    let j = i + 1
    let k = nums.length - 1
    while (j < k) {
      const sum = nums[i] + nums[j] + nums[k]
      if (Math.abs(target - sum) < Math.abs(target - answer)) {
        answer = sum
        if (answer === target) return target
      }
      sum > target ? k-- : j++
    }
  }
  return answer
}
