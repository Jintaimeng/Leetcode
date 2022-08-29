class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                if target == nums[left] and target == nums[right]:
                    return [left, right]
                if target > nums[left]:
                    left += 1
                if target < nums[right]:
                    right -= 1
        return [-1, -1]
