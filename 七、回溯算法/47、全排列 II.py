from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.used = [False for _ in range(len(nums))]
        self.backtracking(sorted(nums), [], res)
        return res

    def backtracking(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]) or self.used[i]:
                continue
            path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums, path, res)
            self.used[i] = False
            path.pop()


def main():
    nums = [1,1,2]
    res = Solution().permuteUnique(nums)
    print(res)


if __name__ == "__main__":
    main()