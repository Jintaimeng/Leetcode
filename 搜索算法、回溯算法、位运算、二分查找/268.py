class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i] ^ (i+1)
        return result