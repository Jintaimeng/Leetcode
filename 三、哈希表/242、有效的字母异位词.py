class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for st in s:
            dict[st] = dict.get(st, 0) + 1
        for st in t:
            dict[st] = dict.get(st, 0) - 1
        for k, v in dict.items():
            if v != 0:
                return False
        return True


def main():
    s = "anagram"
    t = "nagaram"
    res = Solution().isAnagram(s, t)
    print(res)


if __name__ == "__main__":
    main()