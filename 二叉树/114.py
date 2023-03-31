class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes = []
        if not root:
            return self.nodes
        self.add_nodes(root)
        for i in range(len(self.nodes)-1):
            self.nodes[i].left = None
            self.nodes[i].right = self.nodes[i+1]

    def add_nodes(self, node):
        if not node:
            return
        self.nodes.append(node)
        self.add_nodes(node.left)
        self.add_nodes(node.right)