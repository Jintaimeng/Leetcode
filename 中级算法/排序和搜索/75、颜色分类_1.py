#使用插入排序实现
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            for i in range(1, n):
                t = nums[i]
                for j in range(i, -1, -1):
                    if t < nums[j - 1]:
                        nums[j] = nums[j - 1]
                    else:
                        break
                nums[j] = t

def main():
    nums = [2,0,1]
    Solution().sortColors(nums)
    print(nums)

if __name__ == "__main__":
    main()