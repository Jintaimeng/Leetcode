class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = 0
        right = length - 1
        result = list(range(length))
        index = length - 1
        while left <= right:
            leftResult = nums[left] * nums[left]
            rightResult = nums[right] * nums[right]
            if leftResult > rightResult:
                result[index] = leftResult
                left += 1
            else:
                result[index] = rightResult
                right -= 1
            index -= 1
        return result