from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        self.root = root
        self.getConvert(self.root)
        return self.root

    def getConvert(self, node):
        if node is None:
            return
        self.getConvert(node.right)
        node.val += self.pre
        self.pre = node.val
        self.getConvert(node.left)
