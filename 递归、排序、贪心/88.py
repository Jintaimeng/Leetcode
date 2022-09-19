class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        cur = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[i]:
                nums1[cur] = nums1[i]
                i -= 1
            else:
                nums1[cur] = nums2[j]
                j -= 1
            cur -= 1
        while j >= 0:
            nums1[cur] = nums2[j]
            j -= 1
            cur -= 1