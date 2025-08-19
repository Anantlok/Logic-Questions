class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            seen = set()
            for num in row:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)

        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[box_row + i][box_col + j]
                        if num != '.':
                            if num in seen:
                                return False
                            seen.add(num)
        return True
        
        