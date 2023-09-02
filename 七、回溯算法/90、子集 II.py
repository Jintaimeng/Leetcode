from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.used = [False for _ in range(len(nums))]
        self.backtracking(sorted(nums), 0, [], res)
        return res

    def backtracking(self, nums, begin, path, res):
        res.append(path[:])
        if begin == len(nums):
            return
        for i in range(begin, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue
            path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums, i + 1, path, res)
            path.pop()
            self.used[i] = False


def main():
    nums = [1, 2, 2]
    res = Solution().subsetsWithDup(nums)
    print(res)


if __name__ == "__main__":
    main()