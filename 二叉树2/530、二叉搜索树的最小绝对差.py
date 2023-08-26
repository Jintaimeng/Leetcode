import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.pre = None
        self.res = math.inf
        return self.getMinimum(root)

    def getMinimum(self, node):
        if node.left:
            self.res = min(self.res, self.getMinimum(node.left))
        if self.pre and abs(self.pre.val - node.val) < self.res:
            self.res = abs(self.pre.val - node.val)
        self.pre = node
        if node.right:
            self.res = min(self.res, self.getMinimum(node.right))
        return self.res