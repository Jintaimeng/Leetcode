#使用双指针实现
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            p0 = 0
            p2 = n - 1
            p = 0
            while p <= p2:
                if nums[p] == 0:
                    nums[p], nums[p0] = nums[p0], nums[p]
                    if p0 == p:
                        p += 1
                    p0 += 1
                elif nums[p] == 1:
                    p += 1
                elif nums[p] == 2:
                    nums[p], nums[p2] = nums[p2], nums[p]
                    if p2 == p:
                        p += 1
                    p2 -= 1



def main():
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)


if __name__ == "__main__":
    main()