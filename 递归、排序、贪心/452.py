class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        out = 1
        points.sort(key=lambda x: x[0])
        for i in range(1, len(points)):
            if points[i-1][1] < points[i][0]:
                out += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])
        return out