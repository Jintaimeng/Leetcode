# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        self.preOrder(root, res)
        return res

    def preOrder(self, curNode, res):
        if curNode is None:
            return
        res.append(curNode.val)
        self.preOrder(curNode.left, res)
        self.preOrder(curNode.right, res)