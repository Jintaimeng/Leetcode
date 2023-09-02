class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        res = 0
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = memo[i - 1][j]
                if memo[i][j] > res:
                    res = memo[i][j]
        return res == len(s)


def main():
    s = "abc"
    t = "ahbgdc"
    res = Solution().isSubsequence(s, t)
    print(res)


if __name__ == "__main__":
    main()