from typing import List


# 在原有数组的空间内反转数组
def reverse(nums: List[int]):
    len_nums = len(nums)
    for i in range(len_nums):
        j = len_nums - 1 - i
        if i >= j:
            return nums
        nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
  a = [2,3,4,6]
  reverse(a)
  print(a)
