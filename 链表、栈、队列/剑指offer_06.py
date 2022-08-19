class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        stack = []
        cur = head
        while cur != None:
            stack.append(cur.val)
            cur = cur.next
        return stack[::-1]