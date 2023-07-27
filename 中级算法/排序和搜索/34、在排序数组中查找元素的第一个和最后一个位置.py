from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int(l + (r - l) / 2)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                while nums[l] < target:
                    l += 1
                while nums[r] > target:
                    r -= 1
                return [l, r]
        return [-1, -1]

def main():
    nums = [5,7,7,8,8,10]
    target = 6
    res = Solution().searchRange(nums, target)
    print(res)


if __name__ == "__main__":
    main()