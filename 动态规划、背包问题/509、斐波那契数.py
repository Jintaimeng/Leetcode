class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        memo0 = 0
        memo1 = 1
        for i in range(2, n + 1):
            sum = memo0 + memo1
            memo0 = memo1
            memo1 = sum
        return memo1


def main():
    n = 4
    res = Solution().fib(n)
    print(res)


if __name__ == "__main__":
    main()