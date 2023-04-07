class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.s = s
        self.part(0)
        return self.res

    def part(self, left):
        if left == len(self.s):
            self.res.append(self.temp[0: ])
            return
        for right in range(left, len(self.s)):
            if self.s[left, right+1] == self.s[left, right+1][::-1]:
                self.temp.append(self.s[left: right+1])
                self.part(right+1)
                self.temp.pop()