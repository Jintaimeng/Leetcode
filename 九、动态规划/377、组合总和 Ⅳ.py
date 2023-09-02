from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0 for _ in range(target + 1)]
        memo[0] = 1
        for j in range(target + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    memo[j] += memo[j - nums[i]]
        return memo[target]


def main():
    nums = [9]
    target = 3
    res = Solution().combinationSum4(nums, target)
    print(res)


if __name__ == "__main__":
    main()