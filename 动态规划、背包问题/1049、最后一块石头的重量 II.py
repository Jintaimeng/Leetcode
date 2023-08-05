from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        target = s // 2
        memo = [0 for _ in range(target + 1)]
        for i in range(len(stones)):
            for j in range(target, -1, -1):
                if j >= stones[i]:
                    memo[j] = max(memo[j], memo[j - stones[i]] + stones[i])
        return s - memo[target] - memo[target]


def main():
    stones = [31,26,33,21,40]
    res = Solution().lastStoneWeightII(stones)
    print(res)


if __name__ == "__main__":
    main()