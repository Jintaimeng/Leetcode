class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        p = head
        index = 0
        while p is not None:
            if p in nodeList:
                return p
            else:
                nodeList.append(p)
                p = p.next
        return None
