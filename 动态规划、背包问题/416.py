class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        C = total // 2
        n = len(nums)
        memo = [False for _ in range(C + 1)]
        for i in range(C + 1):
            if nums[0] == i:
                memo[i] = True
        for i in range(1, n):
            for j in range(C, nums[i] - 1, -1):
                memo[j] = memo[j] or memo[j - nums[i]]
        return memo[C]