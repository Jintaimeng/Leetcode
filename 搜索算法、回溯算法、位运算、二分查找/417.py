class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.heights = heights
        self.m = len(heights)
        self.n = len(heights[0])
        self.dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.memoP = [[None for _ in range(self.n)] for _ in range(self.m)]
        self.memoA = [[None for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.pacAtl(i, j, "P") and self.pacAtl(i, j, "A"):
                    self.res.append([i, j])
        return self.res

    def pacAtl(self, x, y, s):
        if s == "P":
            if self.memoP[x][y]:
                return self.memoP[x][y]
            if x == 0 or y == 0:
                self.memoP[x][y] = True
                return True
            else:
                self.visited[x][y] = True
                for i in range(4):
                    newx = x + self.dir[i][0]
                    newy = y + self.dir[i][1]
                    if self.isArea(newx, newy) and not self.visited[newx][newy] and self.heights[newx][newy] <= self.heights[x][y] and self.pacAtl(newx, newy, s):
                        self.memoP[x][y] = True
                        self.visited[x][y] = False
                        return True
                self.visited[x][y] = False
                self.memoP[x][y] = False
                return False
        elif s == "A":
            if self.memoA[x][y]:
                return self.memoA[x][y]
            if x == self.m-1 or y == self.n-1:
                self.memoA[x][y] = True
                return True
            else:
                self.visited[x][y] = True
                for i in range(4):
                    newx = x + self.dir[i][0]
                    newy = y + self.dir[i][1]
                    if self.isArea(newx, newy) and not self.visited[newx][newy] and self.heights[newx][newy] <= self.heights[x][y] and self.pacAtl(newx, newy, s):
                        self.memoA[x][y] = True
                        self.visited[x][y] = False
                        return True
                self.visited[x][y] = False
                self.memoA[x][y] = False
                return False

    def isArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n