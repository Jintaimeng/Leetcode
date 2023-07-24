class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        p = headA
        q = headB
        while True:
            if p == q and p is not None:
                return p
            p = p.next
            q = q.next
            if p is None and q is None:
                return None
            if p is None:
                p = headB
            if q is None:
                q = headA
