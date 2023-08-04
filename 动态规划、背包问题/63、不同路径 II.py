from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                memo[i][0] = 1
            else:
                break
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                memo[0][i] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[m - 1][n - 1]


def main():
    obstacleGrid = [[1,0]]
    res = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(res)


if __name__ == "__main__":
    main()