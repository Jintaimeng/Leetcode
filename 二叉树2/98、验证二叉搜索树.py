from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = None
        return self.isValid(root)

    def isValid(self, node):
        if node is None:
            return True
        left = self.isValid(node.left)
        if self.pre and node.val <= self.pre.val:
            return False
        else:
            self.pre = node
        right = self.isValid(node.right)
        return left and right