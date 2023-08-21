# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHight(root) != -1

    def getHight(self, node):
        if node is None:
            return 0
        left = self.getHight(node.left)
        right = self.getHight(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return -1
