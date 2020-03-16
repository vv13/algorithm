from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arrs = nums1 + nums2
        arrs.sort()
        arrs_len = len(arrs)
        if arrs_len % 2 == 1:
          return arrs[arrs_len // 2]
        else:
          return (arrs[arrs_len // 2 - 1] + arrs[arrs_len // 2]) / 2
