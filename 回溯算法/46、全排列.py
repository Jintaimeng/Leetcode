from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.used = [False for _ in range(len(nums))]
        self.backtracking(nums, [], res)
        return res

    def backtracking(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(0, len(nums)):
            if not self.used[i]:
                path.append(nums[i])
                self.used[i] = True
                self.backtracking(nums, path, res)
                path.pop()
                self.used[i] = False


def main():
    nums = [1]
    res = Solution().permute(nums)
    print(res)


if __name__ == "__main__":
    main()