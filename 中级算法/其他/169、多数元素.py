from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        limit = n // 2
        dict = {}
        res = -1
        for i in range(n):
            if nums[i] not in dict.keys():
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
                if dict[nums[i]] > limit:
                    res = nums[i]
                    break
        if res == -1:
            return max(dict.values())
        return res


def main():
    nums = [1]
    res = Solution().majorityElement(nums)
    print(res)


if __name__ == "__main__":
    main()