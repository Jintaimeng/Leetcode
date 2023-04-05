class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(0, self.m):
            for j in range(0, self.n):
                if (i == 0 or i == self.m-1 or j == 0 or j == self.n-1) and self.board[i][j] == "O" and not self.visited[i][j]:
                    self.flip(i, j, False)
        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                if self.board[i][j] == "O" and not self.visited[i][j]:
                    self.flip(i, j, True)

    def isCenter(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def flip(self, x, y, isFlip):
        if isFlip:
            self.board[x][y] = "X"
        self.visited[x][y] = True
        for i in range(4):
            newx = x + self.dir[i][0]
            newy = y + self.dir[i][1]
            if self.isCenter(newx, newy) and self.board[newx][newy] == "O" and not self.visited[newx][newy]:
                self.flip(newx, newy, isFlip)