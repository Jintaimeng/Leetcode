from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        self.res = []
        self.getParenthesis(n)
        return list(set(self.res))

    def getParenthesis(self, num):
        if num == 1:
            return ["()"]
        for i in range(1, num):
            t1 = self.getParenthesis(i)
            t2 = self.getParenthesis(num - i)
            for j in range(len(t1)):
                for k in range(len(t2)):
                    if j == k and (t1[j] + t2[k]) in self.res:
                        continue
                    else:
                        self.res.append(t1[j] + t2[k])



def main():
    n = 3
    res = Solution().generateParenthesis(n)
    print(res)


if __name__ == "__main__":
    main()