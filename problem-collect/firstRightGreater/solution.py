from typing import List


def firstRightGreater(arrs: List[int]) -> List[int]:
    stack = []
    ret = [-1 for i in range(len(arrs))]
    for index, item in enumerate(arrs):
        while stack:
            if item > arrs[stack[-1]]:
                ret[stack.pop()] = item
            else:
                stack.append(index)
                break
        else:
            stack.append(index)
    return ret


ret = firstRightGreater([1, 5, 3, 6, 4, 8, 9, 10])
print(ret)
