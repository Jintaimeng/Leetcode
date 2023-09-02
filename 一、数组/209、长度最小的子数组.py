import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = math.inf
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1
        if res == math.inf:
            return 0
        return res


def main():
    target = 7
    nums = [2,3,1,2,4,3]
    res = Solution().minSubArrayLen(target, nums)
    print(res)


if __name__ == "__main__":
    main()