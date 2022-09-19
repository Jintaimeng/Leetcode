class Node:
    def __init__(self, x: int, next: 'None' = None, random: 'None' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        if head == None:
            return head
        p = head
        map = dict()
        while p is not None:
            newnode = Node(p.val, None, None)
            map[p] = newnode
            p = p.next
        p = head
        while p is not None:
            curnode = map.get(p)
            keyNextNode = p.next
            valueNextNode = map.get(keyNextNode)
            curnode.next = valueNextNode
            keyRandomNode = p.random
            valueRandomNode = map.get(keyRandomNode)
            curnode.random = valueRandomNode
            p = p.next
        return map.get(head)