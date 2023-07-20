from collections import deque
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        current_min = nums[0]
        dq = deque(sorted(nums[2: ]))
        for i in range(1, len(nums)-1):
            if current_min < nums[i] and nums[i] < dq[-1]:
                return True
            if current_min > nums[i]:
                current_min = nums[i]
            if nums[i + 1] == dq[-1]:
                dq.pop()
        return False


def main():
    nums = [1,2,1,2,1,2,1,2,1,2,1,2]
    res = Solution().increasingTriplet(nums)
    print(res)

if __name__ == "__main__":
    main()