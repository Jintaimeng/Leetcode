class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = list(range(len(nums)))
        for i, step in enumerate(nums):
            jump[i] = nums[i] + i
        cur = 0
        maxJump = jump[0]
        while cur < len(nums) and cur <= maxJump:
            if maxJump < jump[cur]:
                maxJump = jump[cur]
            cur += 1
        if cur > len(nums) - 1:
            return True
        return False