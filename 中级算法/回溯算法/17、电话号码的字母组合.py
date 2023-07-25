from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        if len(digits) == 0:
            return self.res
        self.letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                   ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        self.getCombina(digits, len(digits), "")
        return self.res

    def getCombina(self, digits, digLen, t):
        if digLen == 0:
            self.res.append(t)
            return
        letter = self.letters[int(digits[0]) - 2]
        for l in range(len(letter)):
            t = t + letter[l]
            self.getCombina(digits[1:], digLen - 1, t)
            t = t[: -1]


def main():
    digits = "23"
    res = Solution().letterCombinations(digits)
    print(res)


if __name__ == "__main__":
    main()