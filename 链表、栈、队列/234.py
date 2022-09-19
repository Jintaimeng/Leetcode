class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        cur = head
        stack = []
        while cur != None:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        for item in stack[::-1]:
            if cur.val != item:
                return False
            cur - cur.next
        return True