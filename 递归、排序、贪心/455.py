class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        child = 0
        cookie = 0
        res = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
                cookie += 1
                res += 1
            else:
                child += 1
        return res