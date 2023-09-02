from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx = 0
        starty = 0
        count = 1
        res = [[0] * n for _ in range(n)]
        for offset in range(1, n // 2 + 1):
            for j in range(starty, n - offset):
                res[startx][j] = count
                count += 1
            for i in range(startx, n - offset):
                res[i][n - offset] = count
                count += 1
            for j in range(n - offset, starty, -1):
                res[n - offset][j] = count
                count += 1
            for i in range(n - offset, startx, -1):
                res[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        if n % 2 == 1:
            res[n // 2][n // 2] = count
        return res


def main():
    n = 3
    res = Solution().generateMatrix(n)
    print(res)


if __name__ == "__main__":
    main()
