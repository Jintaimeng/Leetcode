from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] > nums[r]:
                if nums[mid] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[l] > nums[mid]:
                    if nums[mid] > target:
                        r = mid -1
                    elif nums[mid] < target:
                        if target > nums[0]:
                            r = mid -1
                        else:
                            l = mid + 1
                elif nums[l] < nums[mid]:
                    if nums[mid] < target:
                        l = mid + 1
                    else:
                        if target > nums[0]:
                            r = mid - 1
                        else:
                            l = mid - 1
                elif nums[l] == nums[mid]:
                    break
        return -1


def main():
    nums = [4,5,6,7,0,1,2]#[1,3, 5]
    target = 0
    res = Solution().search(nums, target)
    print(res)


if __name__ == "__main__":
    main()