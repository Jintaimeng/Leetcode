class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        left = 0
        right = len(res) - 1
        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return " ".join(res)


def main():
    s = "  hello world  "
    res = Solution().reverseWords(s)
    print(res)


if __name__ == "__main__":
    main()