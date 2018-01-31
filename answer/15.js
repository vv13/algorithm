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
  const { positive, negative, numCount } = filterNums(nums)

  if (numCount[0] > 2) results.push([0, 0, 0]) // all 0

  negative.forEach((e) => {
    // includes 0
    if (numCount[0] && numCount[e * -1]) {
      results.push([e, 0, -e])
    }
    // two same
    const r2Same = -1 * e / 2
    const r1Same = -1 * e * 2
    if (numCount[r2Same] >= 2) {
      results.push([e, r2Same, r2Same])
    }
    if (numCount[e] >= 2 && numCount[r1Same]) {
      results.push([e, e, r1Same])
    }
  })

  // other
  const finds = negative.concat(positive)
  for (let i = 0; i < finds.length - 2; i++) {
    const aim = -1 * finds[i]
    let left = i + 1
    let right = finds.length - 1
    while (left < right) {
      if (finds[left] + finds[right] === aim) {
        results.push([finds[i], finds[left], finds[right]])
        left++
        right--
      } else if (finds[left] + finds[right] <= aim) {
        left++
      } else {
        right--
      }
    }
  }

  return results
}

function filterNums(nums) {
  const filterd = []
  const negative = []
  const positive = []
  const numCount = {}
  nums.forEach((e) => {
    numCount[e] = numCount[e] ? numCount[e] + 1 : 1
    if (e !== 0 && numCount[e] === 1) {
      if (e > 0) {
        positive.push(e)
      } else {
        negative.push(e)
      }
    }
  })
  positive.sort((a, b) => a - b)
  negative.sort((a, b) => a - b)
  return {
    positive,
    negative,
    numCount,
  }
}
