from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        next = 0
        for i in range(len(nums)):
            next = max(next, i + nums[i])
            if i == cur:
                if i < len(nums) - 1:
                    res += 1
                    cur = next
                    if cur >= len(nums) - 1:
                        break
                else:
                    break
        return res


def main():
    nums = [2,3,1,1,4]
    res = Solution().jump(nums)
    print(res)


if __name__ == "__main__":
    main()