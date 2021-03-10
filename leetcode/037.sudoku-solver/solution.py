from typing import List



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.runner(board, 0, 0)
        print(1, board)

    def runner(self, board, x, y):
        if x == 9:
            return True
        if y >= 9:
            return self.runner(board, x + 1, 0)
        if board[x][y] != '.':
            return self.runner(board, x, y + 1)
        for i in range(1, 10):
            if self.checkPoint(board, x, y, str(i)):
                board[x][y] = str(i)
                if self.runner(board, x, y + 1):
                    return True
                board[x][y] = '.'
        return False

    def checkPoint(self, board, x, y, v):
        box_index = x // 3 + y // 3
        for i in range(9):
            # check x
            if board[i][y] == v:
                return False
            # check y
            if board[x][i] == v:
                return False
        # check box
        start_x = x // 3 * 3
        start_y = y // 3 * 3
        for check_x in range(start_x, start_x + 3):
            for check_y in range(start_y, start_y + 3):
                if board[check_x][check_y] == v:
                    return False
        return True

