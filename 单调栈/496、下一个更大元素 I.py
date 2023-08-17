from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums1))]
        deque = []
        deque.append(nums2[0])
        for i in range(1, len(nums2)):
            while deque and nums2[i] > deque[-1]:
                if deque[-1] in nums1:
                    res[nums1.index(deque[-1])] = nums2[i]
                deque.pop()
            deque.append(nums2[i])
        return res


def main():
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    res = Solution().nextGreaterElement(nums1, nums2)
    print(res)

if __name__ == "__main__":
    main()
