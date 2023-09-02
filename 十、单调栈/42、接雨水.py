from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        deque = []
        deque.append(0)
        for i in range(1, len(height)):
            while deque and height[i] > height[deque[-1]]:
                right = i
                mid = deque.pop()
                if deque:
                    left = deque[-1]
                    h = min(height[left], height[right]) - height[mid]
                    w = right - left - 1
                    res += (h * w)
            deque.append(i)
        return res


def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = Solution().trap(height)
    print(res)


if __name__ == "__main__":
    main()