from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.isValid(board, k, i, j):
                            board[i][j] = str(k)
                            if self.backtracking(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, num, row, col):
        for i in range(9):
            if board[i][col] == str(num):
                return False
        for j in range(9):
            if board[row][j] == str(num):
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(num):
                    return False
        return True
