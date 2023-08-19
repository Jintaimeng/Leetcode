from collections import deque
from typing import List


class Myqueue:
    def __init__(self):
        self.queue = deque()

    def myPush(self, x):
        while self.queue and self.queue[-1] < x:
            self.queue.pop()
        self.queue.append(x)

    def myPop(self, x):
        if self.queue and self.queue[0] == x:
            self.queue.popleft()

    def getMax(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        res = []
        queue = Myqueue()
        for i in range(k):
            queue.myPush(nums[i])
        res.append(queue.getMax())

        for i in range(k, len(nums)):
            queue.myPop(nums[i - k])
            queue.myPush(nums[i])
            res.append(queue.getMax())
        return res


def main():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 7
    res = Solution().maxSlidingWindow(nums, k)
    print(res)


if __name__ == "__main__":
    main()