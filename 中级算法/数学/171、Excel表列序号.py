import math


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        sum = 0
        mul = 26
        sum_1 = ord(columnTitle[n - 1]) - ord("A") + 1
        for i in range(1, n):
            sum += (ord(columnTitle[n - 1 - i]) - ord("A") + 1) * mul
            mul *= 26
        return int(sum + sum_1)


def main():
    columnTitle = "ZY"
    res = Solution().titleToNumber(columnTitle)
    print(res)


if __name__ == "__main__":
    main()