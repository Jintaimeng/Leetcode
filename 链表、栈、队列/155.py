class MinStack:
    def __init__(self):
        self.min_stack = list()
        self.stack = list()
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            Min = self.min_stack[-1]
            self.min_stack.append(Min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
