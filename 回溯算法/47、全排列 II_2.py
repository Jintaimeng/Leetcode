from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.used = [False for _ in range(len(nums))]
        self.backtracking(nums, [], res)
        return res

    def backtracking(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        use = set()
        for i in range(len(nums)):
            if self.used[i] or nums[i] in use:
                continue
            path.append(nums[i])
            self.used[i] = True
            use.add(nums[i])
            self.backtracking(nums, path, res)
            path.pop()
            self.used[i] = False


def main():
    nums = [1,2,3]
    res = Solution().permuteUnique(nums)
    print(res)


if __name__ == "__main__":
    main()