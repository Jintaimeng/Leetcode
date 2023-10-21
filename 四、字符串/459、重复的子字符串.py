class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n < 1:
            return False
        ss = s[1:] + s[: -1]
        return ss.find(s) != -1


def main():
    s = "abab"
    res = Solution().repeatedSubstringPattern(s)
    print(res)


if __name__ == "__main__":
    main()