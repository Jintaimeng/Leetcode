class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[0 for _ in range(n)] for _ in range(m)]
        self.memo[m - 1][n - 1] = 1
        self.memo[m - 1][n - 2] = 1
        self.memo[m - 2][n - 1] = 1
        for i in range(m):
            self.memo[i][n - 1] = 1
        for i in range(n):
            self.memo[m - 1][i] = 1
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                self.memo[i][j] = self.memo[i][j + 1] + self.memo[i + 1][j]
        return self.memo[0][0]


def main():
    m = 3
    n = 2
    res = Solution().uniquePaths(m, n)
    print(res)


if __name__ == "__main__":
    main()
