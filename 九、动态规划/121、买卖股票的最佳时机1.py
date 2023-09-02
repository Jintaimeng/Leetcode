from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[0, 0] for _ in range(len(prices))]
        memo[0][0] = - prices[0]
        memo[0][1] = 0
        for i in range(1, len(prices)):
            memo[i][0] = max(memo[i - 1][0], - prices[i])
            memo[i][1] = max(memo[i - 1][1], memo[i - 1][0] + prices[i])
        return memo[-1][1]


def main():
    prices = [7,1,5,3,6,4]
    res = Solution().maxProfit(prices)
    print(res)


if __name__ == "__main__":
    main()