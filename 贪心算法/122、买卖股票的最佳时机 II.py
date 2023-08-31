from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) == 1:
            return res
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                res += diff
        return res


def main():
    prices = [7,1,5,3,6,4]
    res = Solution().maxProfit(prices)
    print(res)


if __name__ == "__main__":
    main()