from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[0, 0, 0, 0] for _ in range(len(prices))]
        memo[0][0] = - prices[0] #第一次持有
        memo[0][1] = 0 #第一次不持有
        memo[0][2] = - prices[0] #第二次持有
        memo[0][3] = 0 #第二次不持有
        for i in range(1, len(prices)):
            memo[i][0] = max(memo[i - 1][0], - prices[i])
            memo[i][1] = max(memo[i - 1][1], memo[i - 1][0] + prices[i])
            memo[i][2] = max(memo[i - 1][2], memo[i - 1][1] - prices[i])
            memo[i][3] = max(memo[i - 1][3], memo[i - 1][2] + prices[i])
        return memo[-1][3]


def main():
    prices = [3,3,5,0,0,3,1,4]
    res = Solution().maxProfit(prices)
    print(res)


if __name__ == "__main__":
    main()