# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum - root.val == 0
        targetSum -= root.val
        left = False
        right = False
        if root.left:
            left = self.hasPathSum(root.left, targetSum)
        if root.right:
            right = self.hasPathSum(root.right, targetSum)
        return left or right
