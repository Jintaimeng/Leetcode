from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return res
        map = {}
        map['2'] = "abc"
        map['3'] = "def"
        map['4'] = "ghi"
        map['5'] = "jkl"
        map['6'] = "mno"
        map['7'] = "pqrs"
        map['8'] = "tuv"
        map['9'] = "wxyz"
        k = len(digits)
        self.letterCombina(k, 0, digits, map, "",  res)
        return res

    def letterCombina(self, k, index, digits, map, temp, res):
        if index == k:
            res.append(temp)
            return
        for i in range(len(map[digits[index]])):
            temp += map[digits[index]][i]
            self.letterCombina(k, index + 1, digits, map, temp, res)
            temp = temp[: -1]


def main():
    digits = "23"
    res = Solution().letterCombinations(digits)
    print(res)


if __name__ == "__main__":
    main()