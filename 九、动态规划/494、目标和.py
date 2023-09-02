from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) % 2 != 0:
            return 0
        if sum(nums) < abs(target):
            return 0
        left = (sum(nums) + target) // 2
        memo = [0 for _ in range(left + 1)]
        memo[0] = 1
        for i in range(len(nums)):
            for j in range(left, -1, -1):
                if j >= nums[i]:
                    memo[j] += memo[j - nums[i]]
        return memo[left]


def main():
    nums = [1,1,1,1,1]
    target = 3
    res = Solution().findTargetSumWays(nums, target)
    print(res)


if __name__ == "__main__":
    main()