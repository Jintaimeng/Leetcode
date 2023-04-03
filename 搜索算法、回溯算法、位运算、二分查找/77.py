class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.combine(n, k, 1)
        return self.res

    def combineT(self, n, k, start):
        if len(self.temp) == k:
            self.res.append(self.temp[0: ])
            return
        for i in range(start, n - (k - len(self.temp)) + 2):
            self.temp.append(i)
            self.combineT(n, k, i+1)
            self.temp.pop()