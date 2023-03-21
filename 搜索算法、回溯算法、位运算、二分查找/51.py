class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.col = [False] * n
        self.dia1 = [False] * (2 * n - 1)
        self.dia2 = [False] * (2 * n - 1)
        self.n = n
        self.queens = [] * n
        self.res = []
        self.putQueens(0)
        return self.res

    def putQueens(self, row):
        if row == self.n:
            self.printRes(self.queens)
        else:
            for c in range(self.n):
                if (not self.col[c]) and (not self.dia1[row+c]) and (not self.dia2[row-c+self.n-1]):
                    self.queens.index(row, c)
                    self.col[c] = True
                    self.dia1[row+c] = True
                    self.dia2[row-c+self.n-1] = True
                    self.putQueens(row+1)
                    self.col[c] = False
                    self.dia1[row+c] = False
                    self.dia2[row-c+self.n-1] = False
                    self.queens.pop(row)

    def printRes(self, queens):
        res1 = [] * self.n
        for q in range(len(queens)):
            strq = '.' * self.n
            strq = strq[:queens[q]] + 'Q' + strq[queens[q]+1:]
            res1.append(strq)
        self.res.append(res1)