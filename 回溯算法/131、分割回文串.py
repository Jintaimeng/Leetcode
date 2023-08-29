from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s, 0, [], res)
        return res

    def backtracking(self, s, begin, path, res):
        if begin == len(s):
            res.append(path[:])
            return
        for i in range(begin, len(s)):
            if s[begin: i + 1] == s[begin: i + 1][:: -1]:
                path.append(s[begin: i + 1])
                self.backtracking(s, i + 1, path, res)
                path.pop()


def main():
    s = "aab"
    res = Solution().partition(s)
    print(res)


if __name__ == "__main__":
    main()