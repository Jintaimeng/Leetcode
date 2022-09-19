class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        shead = ListNode(-1)
        stail = shead
        bhead = ListNode(-1)
        btail = bhead
        while head != None:
            if head.val < x:
                stail.next = head
                stail = head
            else:
                btail.next = head
                btail = head
            head = head.next
        stail.next = bhead.next
        btail.next = None
        return shead.next