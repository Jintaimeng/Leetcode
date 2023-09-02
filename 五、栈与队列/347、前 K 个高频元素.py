import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        for i in range(len(nums)):
            if nums[i] in fre.keys():
                fre[nums[i]] += 1
            else:
                fre[nums[i]] = 1
        priQue = []
        for n, f in fre.items():
            heapq.heappush(priQue, (f, n))
            if len(priQue) > k:
                heapq.heappop(priQue)
        res = []
        for i in range(len(priQue)):
            res.append(priQue[i][1])
        return res


def main():
    nums = [1,1,1,2,2,3]
    k = 2
    res = Solution().topKFrequent(nums, k)
    print(res)


if __name__ == "__main__":
    main()