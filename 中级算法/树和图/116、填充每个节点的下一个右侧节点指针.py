from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        dq = deque()
        dq.append(root)
        while dq:
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                if i < n - 1:
                    node.next = dq[0]
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return root