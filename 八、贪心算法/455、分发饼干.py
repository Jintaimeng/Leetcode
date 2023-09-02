from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        res = 0
        index = len(s) - 1
        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and g[i] <= s[index]:
                index -= 1
                res += 1
        return res


def main():
    g = [1,2,3]
    s = [1,1]
    res = Solution().findContentChildren(g, s)
    print(res)


if __name__ == "__main__":
    main()