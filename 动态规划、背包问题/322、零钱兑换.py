import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf for _ in range(amount + 1)]
        memo[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                memo[j] = min(memo[j], memo[j - coins[i]] + 1)
        if memo[amount] == math.inf:
            return -1
        return memo[amount]


def main():
    coins = [2]
    amount = 3
    res = Solution().coinChange(coins, amount)
    print(res)


if __name__ == "__main__":
    main()