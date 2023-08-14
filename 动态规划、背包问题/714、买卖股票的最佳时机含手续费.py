from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = [[0, 0] for _ in range(len(prices))]
        memo[0][0] = - prices[0]
        memo[0][1] = 0
        for i in range(1, len(prices)):
            memo[i][0] = max(memo[i - 1][0], memo[i - 1][1] - prices[i])
            memo[i][1] = max(memo[i - 1][1], memo[i - 1][0] + prices[i] - fee)
        return memo[-1][1]


def main():
    prices = [2,1,4,4,2,3,2,5,1,2]
    fee = 1
    res = Solution().maxProfit(prices, fee)
    print(res)

if __name__ == "__main__":
    main()