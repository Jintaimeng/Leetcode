from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, 0, [], res)
        return res

    def backtracking(self, nums, begin, path, res):
        res.append(path[:])
        if begin == len(nums):
            return
        for i in range(begin, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, res)
            path.pop()


def main():
    nums = [1,2,3]
    res = Solution().subsets(nums)
    print(res)


if __name__ == "__main__":
    main()