from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        for l in lists:
            if l:
                t = l
                while t:
                    pq.put(t.val)
                    t = t.next
        head = ListNode(0)
        p = head
        while not pq.empty():
            p.next = ListNode(pq.get())
            p = p.next
        return head.next