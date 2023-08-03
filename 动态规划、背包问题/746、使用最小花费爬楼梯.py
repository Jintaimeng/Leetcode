from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n + 1)
        memo[0] = 0
        memo[1] = 0
        for i in range(2, n + 1):
            memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2])
        return memo[n]


def main():
    cost = [1,100,1,1,1,100,1,1,100,1]
    res = Solution().minCostClimbingStairs(cost)
    print(res)


if __name__ == "__main__":
    main()