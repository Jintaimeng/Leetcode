class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]
        memo[0] = 0
        memo[1] = 0
        memo[2] = 1
        for i in range(3, n + 1):
            for j in range(1, n // 2 + 1):
                memo[i] = max(j * (i - j), j * memo[i - j], memo[i])
        return memo[n]


def main():
    n = 2
    res = Solution().integerBreak(n)
    print(res)


if __name__ == "__main__":
    main()