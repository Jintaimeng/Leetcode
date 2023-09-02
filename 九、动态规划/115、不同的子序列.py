class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            memo[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
                else:
                    memo[i][j] = memo[i - 1][j]
        return memo[-1][-1]


def main():
    s = "rabbbit"
    t = "rabbit"
    res = Solution().numDistinct(s, t)
    print(res)


if __name__ == "__main__":
    main()