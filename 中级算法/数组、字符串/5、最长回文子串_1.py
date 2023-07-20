#暴力解法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ""
        current_res = ""
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                now_str = s[i: j+1]
                if len(now_str) > len(current_res):
                    if now_str == now_str[::-1]:
                        current_res = now_str
                        break
                else:
                    break

            if len(current_res) > len(res):
                res = current_res
        return res


def main():
    s = ""
    res = Solution().longestPalindrome(s)
    print(res)


if __name__ == "__main__":
    main()