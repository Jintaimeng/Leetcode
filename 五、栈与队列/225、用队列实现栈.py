from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()
        self.count = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.count += 1

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            x = self.queue.popleft()
            self.queue.append(x)
        self.count -= 1
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return self.count == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()