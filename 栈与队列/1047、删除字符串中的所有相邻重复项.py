class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if stack and stack[-1] != s[i]:
                stack.append(s[i])
            elif stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        res = ""
        while stack:
            res = stack.pop() + res
        return res


def main():
    s = "abbaca"
    res = Solution().removeDuplicates(s)
    print(res)

if __name__ == "__main__":
    main()