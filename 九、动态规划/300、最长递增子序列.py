from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)
        return max(memo)


def main():
    nums = [10,9,2,5,3,7,101,18]
    res = Solution().lengthOfLIS(nums)
    print(res)


if __name__ == "__main__":
    main()