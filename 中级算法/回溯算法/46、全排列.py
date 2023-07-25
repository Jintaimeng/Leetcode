from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        p = []
        self.used = [False] * len(nums)
        self.getPer(nums, 0, p)
        return self.res

    def getPer(self, nums, index, p):
        if index == len(nums):
            self.res.append(p[0: ])
            return
        for i in range(len(nums)):
            if not self.used[i]:
                p.append(nums[i])
                self.used[i] = True
                self.getPer(nums, index + 1, p)
                p.pop()
                self.used[i] = False

def main():
    n = [1,2,3]
    res = Solution().permute(n)
    print(res)


if __name__ == "__main__":
    main()