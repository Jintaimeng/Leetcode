from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < k:
            return []
        dict = {}
        for i in range(n):
            if nums[i] not in dict.keys():
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        res = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(res[i][0])
        return result


def main():
    nums = [1]
    k = 1
    res = Solution().topKFrequent(nums, k)
    print(res)


if __name__ == "__main__":
    main()