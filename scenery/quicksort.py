from typing import List


def quicksort(arrs: List[int], left=None, right=None):
    if (left is not None and right is not None) and left >= right:
        return arrs

    left = left or 0
    right = right or len(arrs) - 1
    start = left
    end = left + 1

    while end <= right:
        if arrs[end] < arrs[left]:
            arrs[start + 1], arrs[end] = arrs[end], arrs[start + 1]
            start += 1
        end += 1

    arrs[left], arrs[start] = arrs[start], arrs[left]
    quicksort(arrs, left, start - 1)
    quicksort(arrs, start + 1, right)
    return arrs


test = [2, 76, 9, 5, 2, 1]
quicksort(test)
