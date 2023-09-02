from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.combination(sorted(candidates), 0, 0, target, [], res)
        return res

    def combination(self, candidates, begin, sum, target, temp, res):
        if sum == target:
            res.append(temp[: ])
            return
        for i in range(begin, len(candidates)):
            if sum + candidates[i] <= target:
                temp.append(candidates[i])
                sum += candidates[i]
                self.combination(candidates, i, sum, target, temp, res)
                temp.pop()
                sum -= candidates[i]


def main():
    candidates = [2,3,6,7]
    target = 7
    res = Solution().combinationSum(candidates, target)
    print(res)


if __name__ == "__main__":
    main()