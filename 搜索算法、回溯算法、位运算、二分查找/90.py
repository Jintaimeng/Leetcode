class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.temp = []
        k = len(nums)
        for i in range(1, k + 1):
            self.subset(nums, i, 0)
        self.res.append([])
        return self.res

    def subset(self, nums, k, start):
        if len(self.temp) == k:
            t = self.temp[0: ]
            t.sort()
            if t not in self.res:
                self.res.append(t)
                return
        for i in range(start, len(nums)):
            self.temp.append(nums[i])
            self.subset(nums, k, i+1)
            self.temp.pop()