from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        memo = [0 for _ in range(target + 1)]
        for i in range(len(nums)):
            for j in range(target, -1, -1):
                if nums[i] <= j:
                    memo[j] = max(memo[j], memo[j - nums[i]] + nums[i])
        return memo[target] == target


def main():
    nums = [1,2,3,5]
    res = Solution().canPartition(nums)
    print(res)


if __name__ == "__main__":
    main()