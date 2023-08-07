from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for _ in range(len(s) + 1)]
        memo[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j: i] in wordDict and memo[j]:
                    memo[i] = True
        return memo[len(s)]


def main():
    s = "leetcode"
    wordDict = ["leet", "code"]
    res = Solution().wordBreak(s, wordDict)
    print(res)


if __name__ == "__main__":
    main()