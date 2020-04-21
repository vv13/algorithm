from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sky_vertical = []
        sky_horizon = []
        # 矩阵横向i代表左右视角
        for i in range(len(grid)):
            sky_horizon.append(max(grid[i]))
            vertical = []
            # 矩阵纵向j代表上下视角
            for j in range(len(grid[i])):
                vertical.append(grid[j][i])
            sky_vertical.append(max(vertical))
        increment = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # 当前建筑高度，需取左右视角与横线视角最小的一个
                increment += min(sky_horizon[i], sky_vertical[j]) - grid[i][j]

        return increment
