from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        dic = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dic[nums1[i] + nums2[j]] = dic.get(nums1[i] + nums2[j], 0) + 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                if - (nums3[i] + nums4[j]) in dic:
                    res += dic[- (nums3[i] + nums4[j])]
        return res


def main():
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    res = Solution().fourSumCount(nums1, nums2, nums3, nums4)
    print(res)


if __name__ == "__main__":
    main()