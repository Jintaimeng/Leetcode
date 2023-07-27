import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for num in nums:
            heapq.heappush(hp, num)
            if len(hp) > k:
                heapq.heappop(hp)
        return heapq.heappop(hp)


def main():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    res = Solution().findKthLargest(nums, k)
    print(res)


if __name__ == "__main__":
    main()