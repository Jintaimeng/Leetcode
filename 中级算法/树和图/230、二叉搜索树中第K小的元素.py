from collections import deque


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dq = deque()
        dq.append(("go", root))
        while dq:
            node = dq.pop()
            if node[0] == "print":
                k -= 1
                if k == 0:
                    return node[1].val
            elif node[0] == "go":
                if node[1].right:
                    dq.append(("go", node[1].right))
                dq.append(("print", node[1]))
                if node[1].left:
                    dq.append(("go", node[1].left))