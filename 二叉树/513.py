class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depth = {}
        res = self.findBottom(root)
        return res
    def findBottom(self, root):
        if not root.left and not root.right:
            return root.val
        dep_l = self.getDepth(root.left)
        dep_r = self.getDepth(root.right)
        if dep_l >= dep_r:
            return self.findBottom(root.left)
        elif dep_l < dep_r:
            return self.findBottom(root.right)
    def getDepth(self, node):
        if node in self.depth.keys():
            return self.depth[node]
        if not node:
            return 0
        if not node.left and not node.right:
            self.depth[node] = 1
            return 1
        dep = max(self.getDepth(node.left), self.getDepth(node.right)) + 1
        self.depth[node] = dep
        return dep
