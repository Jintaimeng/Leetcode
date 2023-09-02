from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.getCombine(n, k, 1)
        return self.res

    def getCombine(self, n, k, begin):
        if len(self.temp) == k:
            self.res.append(self.temp[: ])
            return
        for i in range(begin, n + 1):
            self.temp.append(i)
            self.getCombine(n, k, i + 1)
            self.temp.pop()


def main():
    n = 4
    k = 2
    res = Solution().combine(n, k)
    print(res)


if __name__ == "__main__":
    main()