from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        memo = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                memo[i] = memo[i - 1] + 1
        return max(memo)


def main():
    nums = [1,3,5,4,7]
    res = Solution().findLengthOfLCIS(nums)
    print(res)


if __name__ == "__main__":
    main()