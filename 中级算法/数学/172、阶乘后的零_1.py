#直接解法，先求阶乘
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        sum = 1
        for i in range(2, n + 1):
            sum *= i
        count = 0
        while sum >= 10:
            sum, d = divmod(sum, 10)
            if d == 0:
                count += 1
            else:
                break
        return count


def main():
    n = 5
    res = Solution().trailingZeroes(n)
    print(res)


if __name__ == "__main__":
    main()