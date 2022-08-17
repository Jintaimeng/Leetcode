class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        res = 0
        profit = list()
        for i in range(1, len(prices)):
            profit.append(prices[i] - prices[i-1])
        for p in profit:
            if p > 0:
                res += p
        return res