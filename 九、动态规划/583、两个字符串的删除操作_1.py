#思路一
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        res = 0
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

                if memo[i][j] > res:
                    res = memo[i][j]
        return len(word1) - res + len(word2) - res


def main():
    word1 = "sea"
    word2 = "eat"
    res = Solution().minDistance(word1, word2)
    print(res)


if __name__ == "__main__":
    main()