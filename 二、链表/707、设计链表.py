class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.count = 0
        self.dummy_head = LinkNode()

    def get(self, index: int) -> int:
        if index < self.count:
            cur = self.dummy_head.next
            while index > 0:
                cur = cur.next
                index -= 1
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        cur = self.dummy_head
        newNode = LinkNode(val)
        newNode.next = cur.next
        cur.next = newNode
        self.count += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = LinkNode(val)
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.count:
            return
        cur = self.dummy_head
        while index > 0:
            cur = cur.next
            index -= 1
        newNode = LinkNode(val, cur.next)
        cur.next = newNode
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return
        cur = self.dummy_head
        while index > 0:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.count -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)