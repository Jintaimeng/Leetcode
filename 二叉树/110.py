class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        depth_l = self.getDepth(root.left)
        depth_r = self.getDepth(root.right)
        if abs(depth_l - depth_r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, node):
        if not node:
            return 0
        depth_l = self.getDepth(node.left)
        depth_r = self.getDepth(node.right)
        return max(depth_l, depth_r) + 1