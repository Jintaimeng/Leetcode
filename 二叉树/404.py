class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left:
                t = node.left
                if not t.left and not t.right:
                    res += t.val
                else:
                    stack.append(t)
            if node.right:
                t = node.right
                if t.left or t.right:
                    stack.append(t)
        return res