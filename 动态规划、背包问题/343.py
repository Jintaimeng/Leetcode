class Solution:
    def integerBreak(self, n: int) -> int:
        self.n = n
        self.memo = [-1] * (n + 1)
        self.memo[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                self.memo[i] = max(self.memo[i], j * (i-j), j * self.memo[i-j])
        return self.memo[n]