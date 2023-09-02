# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.compare(root.left, root.right)

    def compare(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.compare(node1.left, node2.right) and self.compare(node1.right, node2.left)
        else:
            return False


