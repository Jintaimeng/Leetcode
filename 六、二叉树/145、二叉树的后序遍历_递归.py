# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        self.postOrder(root, res)
        return res

    def postOrder(self, curNode, res):
        if curNode is None:
            return
        self.postOrder(curNode.left, res)
        self.postOrder(curNode.right, res)
        res.append(curNode.val)