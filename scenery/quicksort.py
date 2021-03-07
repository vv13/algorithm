import profile
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


def quicksort1(arrs: List[int], left=None, right=None):
    if (left != None and right != None) and left >= right:
        return arrs

    left = left or 0
    right = right or len(arrs) - 1
    i = left
    j = len(arrs) - 1
    while i != j:
        while arrs[j] >= arrs[left] and j > i:
            j -= 1
        while arrs[i] <= arrs[left] and j > i:
            i += 1
        if i < j:
            arrs[i], arrs[j] = arrs[j], arrs[i]
    arrs[left], arrs[i] = arrs[i], arrs[left]

    quicksort1(arrs, left, i - 1)
    quicksort1(arrs, i + 1, right)
    return arrs


def quicksort2(arrs: List[int]):
    if len(arrs) < 2:
        return arrs

    left = []
    right = []
    base = arrs[0]
    for i in range(1, len(arrs)):
        if base > arrs[i]:
            left.append(arrs[i])
        else:
            right.append(arrs[i])
    return quicksort2(left) + [base] + quicksort2(right)


test = [2, 76, 5, 87, 1, 42, 2, 76, 5, 87, 1,
        42, 2, 76, 5, 87, 1, 42, 2, 76, 5, 87, 1, 42]
print(quicksort2(test))


def profileTest():
    for i in range(10000):
        quicksort2(test)


profile.run('profileTest()')
