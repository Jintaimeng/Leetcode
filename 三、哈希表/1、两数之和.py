from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict.keys():
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i


def main():
    nums = [3,2,4]
    target = 6
    res = Solution().twoSum(nums, target)
    print(res)


if __name__ == "__main__":
    main()