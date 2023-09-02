import math


class Solution:
    def numSquares(self, n: int) -> int:
        memo = [math.inf for _ in range(n + 1)]
        memo[0] = 0
        for i in range(1, n + 1):
            t = i * i
            if t <= n:
                for j in range(t, n + 1):
                    memo[j] = min(memo[j], memo[j - t] + 1)
            else:
                break
        return memo[n]


def main():
    n = 1
    res = Solution().numSquares(n)
    print(res)


if __name__ == "__main__":
    main()