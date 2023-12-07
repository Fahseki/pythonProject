# 请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字1-9在每一行只能出现一次。
# 数字1-9在每一列只能出现一次。
# 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 定义三个二维数组，来存数字是否出现过
        cols = [[0 for a in range(9)] for a in range(10)]  # 列
        rows = [[0 for a in range(9)] for a in range(10)]  # 行
        blocks = [[0 for a in range(9)] for a in range(10)]  # 3*3小块

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    # 存着当前这个数是啥
                    num = int(board[i][j])
                    # 查一下对应的地方是不是出现过
                    if rows[i][num] == 1:
                        return False
                    if cols[j][num] == 1:
                        return False
                    if blocks[(i // 3) * 3 + j // 3][num] == 1:
                        return False
                    # 如果没出现，就在对应位置改成1
                    rows[i][num] = 1
                    cols[j][num] = 1
                    blocks[(i // 3) * 3 + j // 3][num] = 1
        return True


'''
[["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
 '''
'''
i = 0
j = 0
cols = [[0 for a in range(9)] for a in range(10)]  # 列
rows = [[0 for a in range(9)] for a in range(10)]  # 行
blocks = [[0 for a in range(9)] for a in range(10)]  # 3*3小块

while i < 9:
    while j < 9:
        cols = [[0 for a in range(9)] for a in range(10)]  # 列
        rows = [[0 for a in range(9)] for a in range(10)]  # 行
        blocks = [[0 for a in range(9)] for a in range(10)]  # 3*3小块

        if board[i][j] != '.':
            num = int(board[i][j])
            if rows[i][num] == 1:
                return False
            if cols[j][num] == 1:
                return False
            if blocks[i // 3 + j // 3][num] == 1:
                return False

            rows[i][num] = 1
            cols[j][num] = 1
            blocks[i // 3 + j // 3][num] = 1
        j += 1
    j = 0  换行后，j要重新开始循环
    i += 1
'''