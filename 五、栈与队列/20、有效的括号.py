class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif stack and i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif stack and i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif stack and i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0


def main():
    s = "()[]{}"
    res = Solution().isValid(s)
    print(res)


if __name__ == "__main__":
    main()