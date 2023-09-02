from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        res = [0] * len(nums)
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[index] = pow(nums[left], 2)
                left += 1
                index -= 1
            else:
                res[index] = pow(nums[right], 2)
                right -= 1
                index -= 1
        return res


def main():
    nums = [-5,-3,-2,-1]
    res = Solution().sortedSquares(nums)
    print(res)


if __name__ == "__main__":
    main()