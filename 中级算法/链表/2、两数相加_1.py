from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count1 = -1
        count2 = -1
        p = l1
        while p:
            count1 += 1
            p = p.next
        p = l2
        while p:
            count2 += 1
            p = p.next

        len1 = count1
        len2 = count2
        p = l1
        sum1 = 0
        while count1 >= 0:
            sum1 += p.val * (10 ** (len1-count1))
            count1 -= 1
            p = p.next
        p = l2
        sum2 = 0
        while count2 >= 0:
            sum2 += p.val * (10 ** (len2 - count2))
            count2 -= 1
            p = p.next
        res_sum = sum1 + sum2

        count = len(str(res_sum))
        start = 1
        head = ListNode(-1)
        p = head
        while start <= count:
            val = res_sum % 10 #gewei
            node = ListNode(val)
            p.next = node
            p = p.next
            start += 1
            res_sum = res_sum // 10
        return head.next

