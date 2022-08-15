class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newhead = ListNode()
        newhead.next = head
        pre = newhead
        cur = head
        for i in range(left-1):
            pre = pre.next
            cur = cur.next
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return newhead.next