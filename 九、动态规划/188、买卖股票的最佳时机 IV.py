from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = [[0 for _ in range(2 * k)] for _ in range(len(prices))]
        for i in range(2 * k):
            if i % 2 == 0:
                memo[0][i] = - prices[0]
            else:
                memo[0][i] = 0
        for i in range(1, len(prices)):
            memo[i][0] = max(memo[i - 1][0], - prices[i])
            for j in range(1, 2 * k):
                if j % 2 == 1:
                    memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1] + prices[i])
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1] - prices[i])
        return memo[-1][-1]


def main():
    k = 2
    prices = [2,1,4,5,2,9,7]
    res = Solution().maxProfit(k, prices)
    print(res)


if __name__ == "__main__":
    main()