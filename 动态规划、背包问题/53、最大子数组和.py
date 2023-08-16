from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [0 for _ in range(len(nums))]
        memo[0] = nums[0]
        res = memo[0]
        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i - 1] + nums[i])
            res = max(res, memo[i])
        return res


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = Solution().maxSubArray(nums)
    print(res)


if __name__ == "__main__":
    main()