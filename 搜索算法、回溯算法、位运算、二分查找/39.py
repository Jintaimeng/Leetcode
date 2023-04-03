class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.combinationSum(candidates, target)
        self.res = [tuple(sorted(r)) for r in self.res]
        self.res = list(set(self.res))
        return self.res

    def combinaS(self, candidates, target):
        if target == 0:
            self.res.append(self.temp[0:])
            return
        for i in range(0, len(candidates)):
            if candidates[i] <= target:
                self.temp.append(candidates[i])
                target -= candidates[i]
                self.combinaS(candidates, target)
                v = self.temp.pop()
                target += v