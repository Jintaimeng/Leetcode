class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(result - target) > abs(sum - target):
                    result = sum
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return sum
        return result