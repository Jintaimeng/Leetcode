class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.row = len(grid)
        if self.row == 0:
            return 0
        self.col = len(grid[0])
        self.grid = grid
        self.visited = [[False for c in range(self.col)] for r in range(self.row)]
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.res = 0
        for r in range(self.row):
            for c in range(self.col):
                if self.visited[r][c] is False and self.grid[r][c] == "1":
                    self.res += 1
                    self.numLands(r, c)
        return self.res

    def isArea(self, x, y):
        return x >= 0 and x < self.row and y >= 0 and y < self.col

    def numLands(self, x, y):
        self.visited[x][y] = True
        for d in range(len(self.dir)):
            new_x = x + self.dir[d][0]
            new_y = y + self.dir[d][1]
            if self.isArea(new_x, new_y) and self.visited[new_x][new_y] is False and self.grid[new_x][new_y] == "1":
                self.numLands(new_x, new_y)

