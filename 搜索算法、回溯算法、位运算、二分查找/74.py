class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            y = int(mid / n)
            x = mid % n
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                right = mid - 1
            elif matrix[y][x] < target:
                left = mid + 1
        return False