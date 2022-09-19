class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res