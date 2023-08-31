from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = 1
        prediff = 0
        for i in range(0, len(nums) - 1):
            curdiff = nums[i + 1] - nums[i]
            if prediff >= 0 and curdiff < 0 or prediff <= 0 and curdiff > 0:
                res += 1
                prediff = curdiff
        return res


def main():
    nums = [1,17,5,10,13,15,10,5,16,8]
    res = Solution().wiggleMaxLength(nums)
    print(res)


if __name__ == "__main__":
    main()