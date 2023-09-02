from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for st in strs:
            x = 0
            y = 0
            for s in st:
                if s == "0":
                    x += 1
                else:
                    y += 1
            for i in range(m, -1, -1):
                if i >= x:
                    for j in range(n, -1, -1):
                        if j >= y:
                            memo[i][j] = max(memo[i][j], memo[i - x][j - y] + 1)
        return memo[m][n]


def main():
    strs = ["10", "0", "1"]
    m = 1
    n = 1
    res = Solution().findMaxForm(strs, m, n)
    print(res)


if __name__ == "__main__":
    main()