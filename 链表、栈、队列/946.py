class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = list()
        for item in pushed:
            stack.append(item)
            while stack and popped[index] == stack[-1]:
                stack.pop()
                index += 1
        if stack:
            return False
        return True