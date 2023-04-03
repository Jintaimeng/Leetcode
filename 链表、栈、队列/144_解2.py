#非递归方法
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = deque()
        n = ("go", root)
        stack.append(n)
        while len(stack) > 0:
            command = stack.pop()
            if command[0] == "print":
                res.append(command[1].val)
            elif command[0] == "go":
                if command[1].right:
                    node_right = ("go", command[1].right)
                    stack.append(node_right)
                if command[1].left:
                    node_left = ("go", command[1].left)
                    stack.append(node_left)
                stack.append(("print", command[1]))
        return res

