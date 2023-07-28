#二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            mul = mid * mid
            if mul <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


def main():
    x = 8
    res = Solution().mySqrt(x)
    print(res)


if __name__ == "__main__":
    main()
