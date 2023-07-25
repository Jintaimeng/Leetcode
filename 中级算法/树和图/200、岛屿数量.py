from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.used = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.res = 0
        self.direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" and not self.used[i][j]:
                    self.res += 1
                    self.getIsland(grid, i, j)
        return self.res

    def getIsland(self, grid, x, y):
        self.used[x][y] = True
        for i in range(4):
            new_x = x + self.direction[i][0]
            new_y = y + self.direction[i][1]
            if new_x >= 0 and new_x < self.m and new_y >= 0 and new_y < self.n and grid[new_x][new_y] == "1" and not \
            self.used[new_x][new_y]:
                self.getIsland(grid, new_x, new_y)


def main():
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    res = Solution().numIslands(grid)
    print(res)


if __name__ == "__main__":
    main()