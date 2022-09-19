class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        else:
            pointA = headA
            pointB = headB
            while pointA != pointB:
                if pointA is None:
                    pointA = headB
                else:
                    pointA = pointA.next
                if pointB is None:
                    pointB = headA
                else:
                    pointB = pointB.next
            return pointA