from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        rear = len(nums)
        for i in range(len(nums)):
            while rear >= 1 and nums[rear - 1] == val:
                rear -= 1
            if nums[i] == val and i < rear:
                nums[i], nums[rear - 1] = nums[rear - 1], nums[i]
                rear -= 1
                i -= 1
        return rear


def main():
    nums = [0,4,4,0,4,4,4,0,2]
    val = 4
    res = Solution().removeElement(nums, val)
    print(res)


if __name__ == "__main__":
    main()