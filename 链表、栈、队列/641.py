class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = []
        self.length = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) == self.length:
            return False
        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.deque) == self.length:
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.deque:
            return False
        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if not self.deque:
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if not self.deque:
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return not self.deque

    def isFull(self) -> bool:
        return len(self.deque) == self.length