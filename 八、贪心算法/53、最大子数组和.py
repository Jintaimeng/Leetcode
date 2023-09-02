import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = - math.inf
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            if cur > res:
                res = cur
            if cur < 0:
                cur = 0
                continue
        return res


def main():
    nums = [-1]
    res = Solution().maxSubArray(nums)
    print(res)


if __name__ == "__main__":
    main()