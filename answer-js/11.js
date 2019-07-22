/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = (height) => {
  let max = 0
  let left = 0
  let right = height.length - 1
  while (left < right) {
    const result = Math.min(height[left], height[right]) * (right - left)
    if (max < result) max = result
    if (height[left] < height[right]) {
      left += 1
    } else {
      right -= 1
    }
  }
  return max
}
