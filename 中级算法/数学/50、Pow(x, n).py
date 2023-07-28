class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        return self.getPow(x, n) if n > 0 else 1.0 / self.getPow(x, -n)

    def getPow(self, x, N):
        res = 1.0
        x_con = x
        while N > 0:
            if N % 2 == 1:
                res *= x_con
            x_con *= x_con
            N //= 2
        return res


def main():
    x = 2
    n = 10
    res = Solution().myPow(x, n)
    print(res)


if __name__ == "__main__":
    main()