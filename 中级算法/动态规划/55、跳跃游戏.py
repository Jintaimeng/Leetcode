#动态规划 自底向上
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= target:
                target = i
        return target == 0


def main():
    nums = [3,2,1,0,4]
    res = Solution().canJump(nums)
    print(res)


if __name__ == "__main__":
    main()