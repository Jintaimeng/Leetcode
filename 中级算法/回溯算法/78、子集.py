from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.res = [[]]
        if n == 1:
            self.res.append([nums[0]])
            return self.res
        for i in range(1, n):
            self.getSubset(nums, 0, i, [])
        self.res.append(nums)
        return self.res

    def getSubset(self, nums, begin, i, p):
        if begin == i:
            self.res.append(p[0:])
            return
        for j in range(len(nums)):
            p.append(nums[j])
            self.getSubset(nums[j + 1: ], begin + 1, i, p)
            p.pop()

def main():
    nums = [1,2,3]
    res = Solution().subsets(nums)
    print(res)


if __name__ == "__main__":
    main()