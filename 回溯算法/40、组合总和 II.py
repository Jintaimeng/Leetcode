from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.used = [False for _ in range(len(candidates))]
        self.combination2(sorted(candidates), target, 0, 0, [], res)
        return res

    def combination2(self, candidates, target, begin, sum, temp, res):
        if sum == target:
            res.append(temp[: ])
            return
        for i in range(begin, len(candidates)):
            if sum + candidates[i] <= target:
                if i > 0 and candidates[i] == candidates[i - 1] and not self.used[i - 1]:
                    continue
                temp.append(candidates[i])
                sum += candidates[i]
                self.used[i] = True
                self.combination2(candidates, target, i + 1, sum, temp, res)
                temp.pop()
                sum -= candidates[i]
                self.used[i] = False


def main():
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = Solution().combinationSum2(candidates, target)
    print(res)


if __name__ == "__main__":
    main()