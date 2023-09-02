from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, 0, [], res)
        return res

    def backtracking(self, nums, begin, path, res):
        if len(path) >= 2:
            res.append(path[:])
        used = set()
        for i in range(begin, len(nums)):
            if nums[i] in used or (len(path) > 0 and path[-1] > nums[i]):
                continue
            path.append(nums[i])
            used.add(nums[i])
            self.backtracking(nums, i + 1, path, res)
            path.pop()


def main():
    nums = [4,4,3,2,1]
    res = Solution().findSubsequences(nums)
    print(res)


if __name__ == "__main__":
    main()