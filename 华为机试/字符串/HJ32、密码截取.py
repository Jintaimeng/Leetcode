class Solution:
    def getCode(self):
        code = input()
        res = 0
        memo = [[False for _ in range(len(code))] for _ in range(len(code))]
        for i in range(len(code) - 1, -1, -1):
            for j in range(i, len(code)):
                if code[i] == code[j]:
                    if j - i <= 1:
                        memo[i][j] = True
                        res = max(res, j - i + 1)
                    elif memo[i + 1][j - 1]:
                        memo[i][j] = True
                        res = max(res, j - i + 1)
        print(res)


def main():
    Solution().getCode()


if __name__ == "__main__":
    main()