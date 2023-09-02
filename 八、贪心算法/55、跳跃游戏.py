from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        i = 0
        while i <= res:
            res = max(res, i + nums[i])
            if res >= len(nums) - 1:
                return True
            i += 1
        return False


def main():
    nums = [2,5,0,0]
    res = Solution().canJump(nums)
    print(res)


if __name__ == "__main__":
    main()