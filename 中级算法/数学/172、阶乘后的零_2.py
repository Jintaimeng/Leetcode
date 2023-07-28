#求[1， n]中质因子5的个数
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        if n == 0:
            return count
        for i in range(5, n + 1, 5):
            m = i
            while m >= 5:
                m, d = divmod(m, 5)
                if d == 0:
                    count += 1
                else:
                    break
        return count


def main():
    n = 3
    res = Solution().trailingZeroes(n)
    print(res)


if __name__ == "__main__":
    main()