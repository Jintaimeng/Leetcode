import math


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = set()
        while True:
            sum = 0
            for s in str(n):
                s = int(s)
                sum = int(sum + math.pow(s, 2))
            if sum == 1:
                return True
            n = sum
            if sum in seen:
                return False
            seen.add(sum)



def main():
    n = 19
    res = Solution().isHappy(n)
    print(res)


if __name__ == "__main__":
    main()