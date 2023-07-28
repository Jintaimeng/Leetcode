#牛顿迭代法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        x0, C = float(x), float(x)
        while True:
            x1 = 0.5 * (x0 + C / x0)
            if abs(x0 - x1) < 1e-7:
                break
            x0 = x1
        return int(x0)


def main():
    x = 8
    res = Solution().mySqrt(x)
    print(res)


if __name__ == "__main__":
    main()
