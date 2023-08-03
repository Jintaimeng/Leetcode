class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1] * (n + 1)
        for i in range(2, n + 1):
            memo[i] = memo[i - 2] + memo[i - 1]
        return memo[n]


def main():
    n = 3
    res = Solution().climbStairs(n)
    print(res)


if __name__ == "__main__":
    main()