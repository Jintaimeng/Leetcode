class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.count = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.count += 1

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.count -= 1
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            return self.stack1[0]

    def empty(self) -> bool:
        return self.count == 0




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()