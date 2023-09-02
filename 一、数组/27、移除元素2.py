from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


def main():
    nums = [0,4,4,0,4,4,4,0,2]
    val = 4
    res = Solution().removeElement(nums, val)
    print(res)


if __name__ == "__main__":
    main()