from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head
        while fast and n + 1 > 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
