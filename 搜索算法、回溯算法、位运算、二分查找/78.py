class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.temp = []
        k = len(nums)
        for i in range(1, k + 1):
            self.subset(nums, i, 0)
        self.res.append([])
        return self.res

    def subset(self, nums, k, start):
        if len(self.temp) == k:
            self.res.append(self.temp[0: ])
            return
        for i in range(start, len(nums) - (k - len(self.temp)) + 1):
            self.temp.append(nums[i])
            self.subset(nums, k, i+1)
            self.temp.pop()