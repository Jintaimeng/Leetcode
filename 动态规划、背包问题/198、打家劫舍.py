from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [0 for _ in range(len(nums))]
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])
        return memo[-1]


def main():
    nums = [2,7,9,3,1]
    res = Solution().rob(nums)
    print(res)


if __name__ == "__main__":
    main()