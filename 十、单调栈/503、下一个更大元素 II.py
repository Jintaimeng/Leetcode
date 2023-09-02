from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        deque = []
        deque.append(0)
        for i in range(1, len(nums) * 2):
            while deque and nums[i % len(nums)] > nums[deque[-1]]:
                res[deque[-1] % len(nums)] = nums[i % len(nums)]
                deque.pop()
            deque.append(i % len(nums))
        return res


def main():
    nums = [1,2,1]
    res = Solution().nextGreaterElements(nums)
    print(res)


if __name__ == "__main__":
    main()