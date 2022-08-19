class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
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