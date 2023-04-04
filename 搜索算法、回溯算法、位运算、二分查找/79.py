class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.used = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.search(word, i, j):
                    return True
        return False

    def search(self, word, x, y):
        if len(word) == 1:
            return word[0] == self.board[x][y]
        if word[0] == self.board[x][y]:
            self.used[x][y] = True
            for i in range(4):
                newx = x + self.dir[i][0]
                newy = y + self.dir[i][1]
                if newx >= 0 and newx < self.m and newy >= 0 and newy < self.n and not self.used[newx][newy] and self.search(word[1:], newx, newy):
                    return True
            self.used[x][y] = False
        return False