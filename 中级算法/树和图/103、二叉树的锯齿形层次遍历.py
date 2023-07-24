from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        dq = deque()
        dq.append(root)
        left_begin = True
        while dq:
            t = deque()
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                if not left_begin:
                    t.appendleft(node.val)
                elif left_begin:
                    t.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            left_begin = not left_begin
            res.append(list(t))
        return res