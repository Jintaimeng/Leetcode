class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i: i + k] = self.reverse(s[i: i + k])
        return "".join(s)

    def reverse(self, st):
        n = len(st)
        for i in range(n // 2):
            st[i], st[n - i - 1] = st[n - i - 1], st[i]
        return st


def main():
    s = "abcdefgh"
    k = 3
    res = Solution().reverseStr(s, k)
    print(res)


if __name__ == "__main__":
    main()