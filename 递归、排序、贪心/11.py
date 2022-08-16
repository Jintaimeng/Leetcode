class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        res = 0
        while left <= right:
            curArea = (right - left) * min(height[left], height[right])
            if curArea > res:
                res = curArea
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res