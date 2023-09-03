from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next and cur.next.next:
            left = cur.next
            right = cur.next.next
            cur.next = right
            left.next = right.next
            right.next = left
            cur = left.next
        return dummy_head.next

