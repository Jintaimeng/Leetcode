class Solution:
    def minimumTotal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        memo[m-1][n-1] = grid[m-1][n-1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if j+1 >= n:
                    memo[i][j] = memo[i+1][j] + grid[i][j]
                elif i+1 >= m:
                    memo[i][j] = memo[i][j+1] + grid[i][j]
                else:
                    memo[i][j] = min((memo[i + 1][j] + grid[i][j]), (memo[i][j+1] + grid[i][j]))
        return memo[0][0]