from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            xx = ['.'] * 9
            yy = ['.'] * 9
            for y in range(9):
                if board[y][x] in xx and board[y][x] != '.':
                    return False
                else:
                    xx[y] = board[y][x]

                if board[x][y] in yy and board[x][y] != '.':
                    return False
                else:
                    yy[y] = board[x][y]

                if x < 3 and y < 3:
                    offset_x = x * 3
                    offset_y = y * 3
                    card = []
                    for cardx in range(offset_x, offset_x + 3):
                        for cardy in range(offset_y, offset_y + 3):
                            if board[cardx][cardy] not in card:
                                card.append(board[cardx][cardy])
                            elif board[cardx][cardy] != '.':
                                return False
        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num == '.':
                    continue
                box_index = x // 3 * 3 + y // 3

                rows[x][num] = rows[x].get(num, 0) + 1
                columns[y][num] = columns[y].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                if rows[x][num] > 1 or columns[y][num] > 1 or boxes[box_index][num] > 1:
                    return False
        return True


input = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]]

result = Solution().isValidSudoku(input)
print(result)
