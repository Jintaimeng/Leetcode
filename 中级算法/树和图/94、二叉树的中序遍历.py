from collections import deque
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        dq = deque()
        dq.append(("go", root))
        while dq:
            node = dq.pop()
            if node[0] == "print":
                res.append(node[1].val)
            elif node[0] == "go":
                if node[1].right:
                    dq.append(("go", node[1].right))
                dq.append(("print", node[1]))
                if node[1].left:
                    dq.append(("go", node[1].left))
        return res