from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0 for _ in range(amount + 1)]
        memo[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                memo[j] += memo[j - coins[i]]
        return memo[amount]


def main():
    amount = 10
    coins = [10]
    res = Solution().change(amount, coins)
    print(res)


if __name__ == "__main__":
    main()