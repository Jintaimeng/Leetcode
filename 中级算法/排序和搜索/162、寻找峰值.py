import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.n = len(nums)
        self.nums = nums
        r = self.n - 1
        l = 0
        while l <= r:
            mid = int(l + (r - l) / 2)
            midNum = self.getNum(mid)
            leftNum = self.getNum(mid - 1)
            rightNum = self.getNum(mid + 1)
            if midNum > leftNum and midNum > rightNum:
                return mid
            elif midNum < rightNum:
                l = mid + 1
            elif midNum < leftNum:
                r = mid - 1

    def getNum(self, index):
        if index == -1 or index == self.n:
            return -math.inf
        else:
            return self.nums[index]


def main():
    nums = [1,2,1,3,5,6,4]
    res = Solution().findPeakElement(nums)
    print(res)


if __name__ == "__main__":
    main()