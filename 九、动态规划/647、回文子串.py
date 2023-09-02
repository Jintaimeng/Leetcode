class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        memo[i][j] = True
                    else:
                        memo[i][j] = memo[i + 1][j - 1]
                if memo[i][j]:
                    res += 1
        return res


def main():
    s = "abc"
    res = Solution().countSubstrings(s)
    print(res)


if __name__ == "__main__":
    main()