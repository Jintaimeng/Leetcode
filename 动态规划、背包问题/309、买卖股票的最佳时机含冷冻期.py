from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[0, 0, 0, 0] for _ in range(len(prices))]
        memo[0][0] = - prices[0] #持股
        memo[0][1] = 0 #保持卖出
        memo[0][2] = 0 #卖股
        memo[0][3] = 0 #冷冻期
        for i in range(1, len(prices)):
            memo[i][0] = max(memo[i - 1][0], memo[i - 1][3] - prices[i], memo[i - 1][1] - prices[i])
            memo[i][1] = max(memo[i - 1][1], memo[i - 1][3])
            memo[i][2] = memo[i - 1][0] + prices[i]
            memo[i][3] = memo[i - 1][2]
        return max(memo[-1][1], memo[-1][2], memo[-1][3])


def main():
    prices = [1,2,3,0,2]
    res = Solution().maxProfit(prices)
    print(res)


if __name__ == "__main__":
    main()