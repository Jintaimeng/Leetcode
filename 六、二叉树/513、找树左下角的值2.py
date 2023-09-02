#递归
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.maxDepth = -1
        self.findBottom(root, 1)
        return self.res

    def findBottom(self, node, depth):
        if node.left is None and node.right is None:
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.res = node.val
            return
        if node.left:
            depth += 1
            self.findBottom(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.findBottom(node.right, depth)
            depth -= 1
