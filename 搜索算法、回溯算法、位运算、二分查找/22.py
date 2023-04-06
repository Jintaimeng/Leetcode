class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.memo = {}
        return self.generateP(n)

    def generateP(self, n):
        if n == 1:
            return ["()"]
        if n in self.memo.keys():
            return self.memo[n]
        temp = []
        for j in range(1, n//2+1):
            t1 = self.generateP(j)
            self.memo[j] = t1
            t2 = self.generateP(n-j)
            self.memo[n-j] = t2
            for i in range(len(t1)):
                for k in range(len(t2)):
                    temp.append(t1[i] + t2[k])
                    temp.append(t2[k] + t1[i])
        t = self.generateP(n-1)
        for i in range(len(t)):
            temp.append("(" + t[i] + ")")
        return list(set(temp))
