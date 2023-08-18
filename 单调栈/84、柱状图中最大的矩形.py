from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights.insert(0, 0)
        heights.append(0)
        deque = []
        deque.append(0)
        for i in range(1, len(heights)):
            while deque and heights[i] < heights[deque[-1]]:
                right = i
                mid = deque.pop()
                if deque:
                    left = deque[-1]
                    h = heights[mid]
                    w = right - left - 1
                    res = max(res, h * w)
            deque.append(i)
        return res


def main():
    height = [2,4]
    res = Solution().largestRectangleArea(height)
    print(res)


if __name__ == "__main__":
    main()