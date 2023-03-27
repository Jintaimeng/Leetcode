class Solution:
    def isValid(self, s: str) -> bool:
        flag = True
        dq = deque()
        for ss in s:
            if ss == "(" or ss == "{" or ss == "[":
                dq.append(ss)
            elif len(dq) > 0 and ((ss == ")" and dq[-1] != "(") or (ss == "}" and dq[-1] != "{") or (ss == "]" and dq[-1] != "[")):
                flag = False
                break
            elif len(dq) == 0 and (ss == ")" or ss == "}" or ss == "]"):
                flag = False
                break
            else:
                dq.pop()
        return len(dq) == 0 and flag