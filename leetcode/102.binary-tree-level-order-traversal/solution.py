from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        search = [root]
        while len(search) > 0:
            size = len(search)
            target = []
            for _ in range(size):
                s = search.pop(0)
                target.append(s.val)
                if s.left:
                    search.append(s.left)
                if s.right:
                    search.append(s.right)
            result.append(target)
        return result


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def bfs(nodeList: List[TreeNode], result: List[int]):
            if len(nodeList) == 0:
                return
            arrs = []
            next_arrs = []
            for node in nodeList:
                arrs.append(node.val)
                if node.left:
                    next_arrs.append(node.left)
                if node.right:
                    next_arrs.append(node.right)
            result.append(arrs)
            bfs(next_arrs, result)
        result = []
        bfs([root], result)
        return result


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(node: TreeNode, deep: int, res):
            if not node:
                return
            if deep == len(res):
                res.append([])
            res[deep].append(node.val)
            dfs(node.left, deep + 1, res)
            dfs(node.right, deep + 1, res)
        dfs(root, 0, res)
        return res
