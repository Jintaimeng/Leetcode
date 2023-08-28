from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.combination(k, n, 1, [], res)
        return res

    def combination(self, k, n, begin, temp, res):
        if sum(temp) == n and len(temp) == k:
            res.append(temp[: ])
            return
        for i in range(begin, 9 - (k - len(temp)) + 2):
            temp.append(i)
            if len(temp) <= k:
                self.combination(k, n, i + 1, temp, res)
            temp.pop()


def main():
    k = 3
    n = 9
    res = Solution().combinationSum3(k, n)
    print(res)


if __name__ == "__main__":
    main()