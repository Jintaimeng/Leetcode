class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor < 0 and dividend > divisor) or \
                (dividend > 0 and divisor > 0 and dividend < divisor):
            return 0
        count = 1
        sum = abs(divisor)
        while sum <= abs(dividend):
            sum += abs(divisor)
            count += 1
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            return count - 1
        else:
            return -(count - 1)


def main():
    dividend = -7
    divisor = -3
    res = Solution().divide(dividend, divisor)
    print(res)


if __name__ == "__main__":
    main()