class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        if len(nums) == 0:
            return self.res
        self.used = [False for j in range(len(nums))]
        self.perm(0, [])
        return self.res

    def perm(self, index, p):
        if index == len(self.nums):
            pt = p[0:]
            self.res.append(pt)
            return
        else:
            for i in range(len(self.nums)):
                if not self.used[i]:
                    p.append(self.nums[i])
                    self.used[i] = True
                    self.perm(index + 1, p)
                    p.pop()
                    self.used[i] = False