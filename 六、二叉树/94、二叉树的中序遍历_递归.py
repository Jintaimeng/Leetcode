# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        self.inOrder(root, res)
        return res

    def inOrder(self, curNode, res):
        if curNode is None:
            return
        self.inOrder(curNode.left, res)
        res.append(curNode.val)
        self.inOrder(curNode.right, res)