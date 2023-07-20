#运用进位carry
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        carry = []
        currents = []
        index = -1
        while p and q:
            if index == -1:
                current = p.val + q.val
            else:
                current = p.val + q.val + carry[index]
            if current >= 10:
                carry.append(current // 10)
                currents.append(current % 10)
            else:
                carry.append(0)
                currents.append(current)
            index += 1
            p = p.next
            q = q.next
        while p:
            if index == -1:
                current = p.val
            else:
                current = p.val + carry[index]
            if current >= 10:
                carry.append(current // 10)
                currents.append(current % 10)
            else:
                carry.append(0)
                currents.append(current)
            index += 1
            p = p.next
        while q:
            if index == -1:
                current = q.val
            else:
                current = q.val + carry[index]
            if current >= 10:
                carry.append(current // 10)
                currents.append(current % 10)
            else:
                carry.append(0)
                currents.append(current)
            index += 1
            q = q.next
        if carry[-1] != 0:
            currents.append(carry[-1])
        head = ListNode(-1)
        p = head
        for i in range(len(currents)-1, -1, -1):
            val = currents[i]
            node = ListNode(val)
            p.next = node
            p = p.next
        return head.next
