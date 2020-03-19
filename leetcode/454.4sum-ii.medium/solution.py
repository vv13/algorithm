from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count, map = 0, {}
        for a in A:
            for b in B:
                self.counter(map, a + b)
        for c in C:
            for d in D:
                count += map.get(-c-d, 0)
        return count
        


    def counter(self, map, target):
        if target not in map:
            map[target] = 1
        else:
            map[target] += 1
