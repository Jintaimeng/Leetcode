from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtracking(s, 0, 0, "", res)
        return res

    def backtracking(self, s, begin, pointSum, path, res):
        if pointSum == 3 and self.isValid(s, begin, len(s)):
            res.append(path + s[begin: len(s)])
            return
        if pointSum > 3:
            return
        for i in range(begin, len(s)):
            if self.isValid(s, begin, i + 1):
                pointSum += 1
                self.backtracking(s, i + 1, pointSum, path + s[begin: i + 1] + ".", res)
                pointSum -= 1

    def isValid(self, s, start, end):
        if start >= end:
            return False
        if s[start] == '0' and (start + 1) != end:
            return False
        return int(s[start: end]) >=0 and int(s[start: end]) <= 255


def main():
    s = "25525511135"
    res = Solution().restoreIpAddresses(s)
    print(res)


if __name__ == "__main__":
    main()