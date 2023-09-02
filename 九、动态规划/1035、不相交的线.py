from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        res = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
                res = max(res, memo[i][j])
        return res


def main():
    nums1 = [1,4,2]
    nums2 = [1,2,4]
    res = Solution().maxUncrossedLines(nums1, nums2)
    print(res)


if __name__ == "__main__":
    main()