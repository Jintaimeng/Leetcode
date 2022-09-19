class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            p = head.next
            if p is None:
                return head
            else:
                head.next = None
                while p is not None:
                    q = p.next
                    p.next = head
                    head = p
                    p = q
                return head