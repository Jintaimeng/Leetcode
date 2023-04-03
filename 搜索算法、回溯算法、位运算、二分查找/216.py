class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.combinaS3(k, n, 1)
        return self.res

    def combinaS3(self, k, n, start):
        if len(self.temp) == k and n == 0:
            self.res.append(self.temp[0: ])
            return
        for i in range(start, 10):#9-(k-len(self.temp)) + 1
            if i <= n:
                self.temp.append(i)
                n -= i
                self.combinaS3(k, n, i+1)
                self.temp.pop()
                n += i
