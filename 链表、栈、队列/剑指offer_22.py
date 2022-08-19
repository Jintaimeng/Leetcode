class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        stack = []
        cur = head
        while cur != None:
            stack.append(cur)
            cur = cur.next
        for i in range(k-1):
            stack.pop()
        return stack[-1]