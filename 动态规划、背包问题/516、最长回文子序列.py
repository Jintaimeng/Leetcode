class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        memo[i][j] = j - i + 1
                    else:
                        memo[i][j] = memo[i + 1][j - 1] + 2
                else:
                    memo[i][j] = max(memo[i + 1][j], memo[i][j - 1])
        return memo[0][-1]


def main():
    s = "cbbd"
    res = Solution().longestPalindromeSubseq(s)
    print(res)


if __name__ == "__main__":
    main()