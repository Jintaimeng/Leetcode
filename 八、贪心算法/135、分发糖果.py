from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candys = [1] * len(ratings)
        for i in range(len(ratings) - 1, -1, -1):
            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                candys[i] = candys[i + 1] + 1
        for i in range(len(ratings)):
            if i >= 1 and ratings[i] > ratings[i - 1]:
                candys[i] = max(candys[i], candys[i - 1] + 1)
        return sum(candys)


def main():
    ratings = [1,2,87,87,87,2,1]
    res = Solution().candy(ratings)
    print(res)


if __name__ == "__main__":
    main()