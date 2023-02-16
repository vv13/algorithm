from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(searchList: List[int], path: List[int], target: int, result: List[List[int]]):
            if target == 0:
                result.append(path)
                return
            elif target < 0:
                return
            for i in range(len(searchList)):
                dfs(searchList[i:], path + [searchList[i]], target - searchList[i], result)

        dfs(candidates, [], target, result)
        return result

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(searchList: List[int], path: List[int], target: int, start: int, result: List[List[int]]):
            if target == 0:
                result.append(path[:])
                return
            elif target < 0:
                return
            for i in range(start, len(searchList)):
                path.append(searchList[i])
                dfs(searchList, path, target - searchList[i], start, result)
                path.pop()

        dfs(candidates, [], target, 0, result)
        return result
