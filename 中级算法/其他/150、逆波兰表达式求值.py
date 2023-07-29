from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()
        fh = ['+', '-', '*', '/']
        for t in tokens:
            if t in fh:
                a = dq.pop()
                b = dq.pop()
                if t == fh[0]:
                    dq.append(a + b)
                elif t == fh[1]:
                    dq.append(b - a)
                elif t == fh[2]:
                    dq.append(a * b)
                else:
                    dq.append(int(b / a))
            else:
                dq.append(int(t))
        return dq[0]


def main():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    res = Solution().evalRPN(tokens)
    print(res)

if __name__ == "__main__":
    main()