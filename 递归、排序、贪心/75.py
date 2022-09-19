class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            for j in range(0, i+1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]