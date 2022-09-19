class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return None
        else:
            p1 = list1
            p2 = list2
            p = ListNode()
            head = p
            while p1 is not None or p2 is not None:
                if p1 is not None and p2 is not None:
                    if p1.val < p2.val:
                        p.next = p1
                        p1 = p1.next
                        p = p.next
                    else:
                        p.next = p2
                        p2 = p2.next
                        p = p.next
                elif p1 is None:
                    p.next = p2
                    p2 = p2.next
                    p = p.next
                elif p2 is None:
                    p.next = p1
                    p1 = p1.next
                    p = p.next
            return head.next