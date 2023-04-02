class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        depth_left = self.minDepth(root.left)
        depth_right = self.minDepth(root.right)
        if depth_left == 0:
            depth_left = depth_right
        if depth_right == 0:
            depth_right = depth_left
        return min(depth_left, depth_right) + 1