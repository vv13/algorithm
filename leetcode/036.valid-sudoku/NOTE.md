对于每一个 board 中的元素来讲，必须满足：
- 元素所在行不允许重复
- 元素所在列不允许重复
- 元素所在方格不允许重复

判定是否重复，可以使用字典来进行记录值是否出现过，因此通过数组加字典的形式，就可以在遍历时，将元素记录到出现过的相应行列的字典中：
```
def checkRowRepeat(board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                rows[x][num] = rows[x].get(num, 0) + 1
                if rows[x][num] > 1:
                    return False
        return True
def checkColRepeat(board: List[List[str]]) -> bool:
        columns = [{} for i in range(9)]
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                columns[y][num] = columns[y].get(num, 0) + 1
                if columns[x][num] > 1:
                    return False
        return True
```

还有一种情况是判断元素所在的 3x3 中是否重复，为了便于记录，可以对单元格进行编号：
![](./36_boxes_2.png)

计算坐标所处的单元格的公式为：`row // 3 * 3 + col // 3`，因此我们转化为与按行按列同样的问题:
```
def checkColRepeat(board: List[List[str]]) -> bool:
        boxes = [{} for i in range(9)]
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                box_index = x // 3 + 3 y // 3
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                if box_index[x][num] > 1:
                    return False
        return True
```

最后，为了效率原因，将 3 个遍历方法进行合并后，则为最优解。
