from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = ['.' * n for _ in range(n)]
        res = []
        self.backtracking(chessboard, n, 0, res)
        return res

    def backtracking(self, chessboard, n, row, res):
        if row == n:
            res.append(chessboard[:])
            return
        for i in range(n):
            if self.isValid(chessboard, row, i):
                chessboard[row] = chessboard[row][: i] + 'Q' + chessboard[row][i + 1:]
                self.backtracking(chessboard, n, row + 1, res)
                chessboard[row] = chessboard[row][: i] + '.' + chessboard[row][i + 1:]

    def isValid(self, chessboard, row, col):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True


def main():
    n = 4
    res = Solution().solveNQueens(n)
    print(res)


if __name__ == "__main__":
    main()