class Solution:
    def rob(self, nums: List[int]) -> int:
        self.n = len(nums)
        if self.n == 0:
            return 0
        self.memo = [-1] * self.n
        self.memo[self.n-1] = nums[self.n-1]
        for i in range(self.n-2, -1, -1):
            for j in range(i, self.n):
                self.memo[i] = max(self.memo[i], nums[j] + (self.memo[j+2] if j+2 < n else 0))
        return self.memo[0]    