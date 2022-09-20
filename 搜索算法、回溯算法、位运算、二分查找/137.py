class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = [0] * 32
        for i in range(len(nums)):
            num = nums[i]
            for j in range(32):
                if num >> j & 1 == 1:
                    cnt[j] += 1
        ans = 0
        for i in range(32):
            if cnt[i] % 3 == 1:
                num = 1 << i
                ans += num
        return ans if cnt[31] % 3 == 0 else ~(ans ^ 0xffffffff)