class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.countN(root)
        return self.count
    def countN(self, node):
        if node:
            self.count += 1
            self.countN(node.left)
            self.countN(node.right)