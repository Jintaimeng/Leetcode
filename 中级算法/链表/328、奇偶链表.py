class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head_odd = head
        head_even = head.next
        o = head_odd
        e = head_even
        p = head_even.next
        count = 3
        while p:
            if count % 2 == 0:
                e.next = p
                e = e.next
            else:
                o.next = p
                o = o.next
            p = p.next
            count += 1

        o.next = head_even
        e.next = None
        return head_odd