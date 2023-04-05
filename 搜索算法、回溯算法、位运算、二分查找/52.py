class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.col = [False for _ in range(n)]
        self.dia1 = [False for _ in range(n * 2 - 1)]
        self.dia2 = [False for _ in range(n * 2 - 1)]
        self.n = n
        self.NQ(0)
        return self.res

    def NQ(self, index):
        if index == self.n:
            self.res += 1
        for i in range(self.n):
            if not self.col[i] and not self.dia1[i+index] and not self.dia2[index-i+self.n-1]:
                self.col[i] = True
                self.dia1[index+i] = True
                self.dia2[index-i+self.n-1] = True
                self.NQ(index + 1)
                self.col[i] = False
                self.dia1[index+i] = False
                self.dia2[index-i+self.n-1] = False