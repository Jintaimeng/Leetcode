class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        res = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])
                res = max(res, memo[i][j])
        return res


def main():
    text1 = "abcde"
    text2 = "ace"
    res = Solution().longestCommonSubsequence(text1, text2)
    print(res)


if __name__ == "__main__":
    main()